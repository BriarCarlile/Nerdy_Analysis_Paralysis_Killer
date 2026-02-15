README
--
I like to buy stuff from time to time, but often find it painful to choose the best option among products - insert data and Pandas!

## What it does
This "application" (very basic right now) takes a spreadsheet where a number of products are compared via numerical values.

### Sample input:
| Brand        |Product|Price|Capacity|
|--------------|---|---|---|
| Super-Duper  |The Duper|150|20|
| Not So Duper | Just Sad | 500 | 5|


### Sample output:
| Brand        | Product   | Price | Capacity | Apartment-weighted | Apartment-weighted-rank | weighted-rank-average-rank | weighted-rank-rank-consistency |
|--------------|-----------|-------|----------|--------------------|-------------------------|----------------------------|--------------------------------|
| Super-Duper  | The Duper | 150   | 20       | 1.0                | 1.0                     | 1.0                        | 1.0                            
| Not So Duper | Just Sad  | 500   | 5        | 0.0                | 3.0                     | 3.0                        | 3.0                            
| Kinda Meh    | Mehza     | 300   | 15       | 0.65238            | 2.0                     | 2.0                        | 2.0                            

### But where do the weights come from?
You can specify weights and relevant columns via a config:
```json
{
  "file_name": "sample_data_sets/random_products.csv",
  "column_headers_row": "1",
  "column_headers_column_start": "A",
  "data_column_start": "B",
  "data_column_end": "",
  "data_row_start": "2",
  "data_row_end": "",
  "metrics": {
    "Price": { "direction": "lower" },
    "Capacity": { "direction": "higher" }
  },
  "profiles": {
    "Apartment": {
      "Price": 15,
      "Capacity": 85
    }
  }
}
```