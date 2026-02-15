import plotly.express as px
import plotly.graph_objects as go
def create_radar_chart(df, column):

    # valid_values = [metric for metric in metrics if metric in df.columns]
    items = list(df.iloc[:, 1])
    radar = px.line_polar(df, r=column, theta=items, line_close=True)
    radar.show()

def create_multiple_radar_chart(df, columns, graph_name):
    items = list(df.iloc[:, 1])
    running_minimum = 1
    running_maximum = 0


    fig = go.Figure()
    for column in columns:
        col_data = df[column]
        running_minimum = min(running_minimum, col_data.min())
        running_maximum = max(running_maximum, col_data.max())
        fig.add_trace(
            go.Scatterpolar(
                r=df[column],
                theta=items,
                fill="toself",
                name=column
            )
        )

    minimum_buffer = (running_maximum - running_minimum) / 10
    fig.update_layout(
        title=graph_name,
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[running_minimum - minimum_buffer, running_maximum]
            )
        ),
        showlegend=True,
    )

    fig.show()
