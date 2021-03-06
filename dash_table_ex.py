import dash
import dash_table
import pandas as pd

app = dash.Dash(name='table1', sharing=True, server=server, url_base_pathname='/table1/')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("rows"),
)

if __name__ == '__main__':
    app.run_server(debug=True)