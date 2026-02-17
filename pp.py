import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# READ DATA
df = pd.read_excel("Book1.xlsx")

app = Dash(__name__)
# CARD STYLE (makes it look premium)
card_style = {
    "background": "#f5f5f5",
    "padding": "20px",
    "borderRadius": "10px",
    "textAlign": "center",
    "width": "180px",
    "boxShadow": "2px 2px 10px rgba(0,0,0,0.1)"
}

# ---- LAYOUT ----
app.layout = html.Div([

    # HEADER
    html.H1("🎓 Student Performance Dashboard",
            style={"textAlign": "center"}),

    # KPI CARDS
    html.Div([

        html.Div([
            html.H3("Total Students"),
            html.H2(df["name"].nunique())
        ], style=card_style),

        html.Div([
            html.H3("Average Marks"),
            html.H2(round(df["marks"].mean(), 2))
        ], style=card_style),

        html.Div([
            html.H3("Highest Marks"),
            html.H2(df["marks"].max())
        ], style=card_style),

        html.Div([
            html.H3("Lowest Marks"),
            html.H2(df["marks"].min())
        ], style=card_style),

    ], style={"display": "flex", "gap": "20px",
              "justifyContent": "center"}),

    # DROPDOWN FILTER
    html.Br(),

    dcc.Dropdown(
        options=[{"label": i, "value": i}
                 for i in df["name"].unique()],
        multi=True,
        value=df["name"].unique().tolist(),
        id="filter",
        style={"width": "60%", "margin": "auto"}
    ),

    html.Br(),

    # CHARTS
    dcc.Graph(id="bar_chart"),
    dcc.Graph(id="pie_chart")

])


# ---- CALLBACK ----
@app.callback(
    Output("bar_chart", "figure"),
    Output("pie_chart", "figure"),
    Input("filter", "value")
)
def update_dashboard(selected):

    filtered_df = df[df["name"].isin(selected)]

    bar_fig = px.bar(
        filtered_df,
        x="name",
        y="marks",
        color="name",
        title="Marks by Student"
    )

    pie_fig = px.pie(
        filtered_df,
        names="name",
        values="marks",
        title="Marks Distribution"
    )

    return bar_fig, pie_fig


app.run(debug=True)
