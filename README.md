# The immo-eliza-ml machine learning project

## Project description

<img align="right" height="200" src="https://assets.everspringpartners.com/dims4/default/5c1df5b/2147483647/strip/true/crop/1400x800+0+0/resize/1600x914!/format/webp/quality/90/?url=http%3A%2F%2Feverspring-brightspot.s3.us-east-1.amazonaws.com%2Ffe%2F06%2Ff23661be455e97d009c6ae418995%2Freal-estate-finance.jpg" />

Real estate business needs fast and efficient tools to take advantageous decisions. Automatic price estimator is a handy tool that can boost the work productivity of real estate projects and navigate the clients in the sea of real estate offers. 

The immo-eliza-ml program is an example of such a tool. With the help of such features as location and living area of the apartment of the house it can rapidly predict the price of the property. 

## Usage
To use the API please access https://immo-eliza-deployment-latest.onrender.com/
Use ```/predict``` path to get the price estimations.
To do this, please send the post request in the following format:
```
{
  "property_id": 999999999,
  "price": 0,
  "locality_name": "brussel",
  "postal_code": 1000,
  "latitude": 50.872696,
  "longitude": 4.315854,
  "property_type": "APARTMENT",
  "property_subtype": "APARTMENT",
  "type_of_sale": "BUY_REGULAR",
  "number_of_rooms": 2,
  "living_area": 60,
  "number_of_rooms": 3.0,
  "living_area": 92.0,
  "kitchen_type": "HYPER_EQUIPPED",
  "fully_equipped_kitchen": 1.0,
  "furnished": 0.0,
  "open_fire": 0.0,
  "terrace": 1.0,
  "terrace_area": 14.0,
  "garden": 0.0,
  "garden_area": 0.0,
  "surface_of_good": 113.0,
  "number_of_facades": 3.0,
  "swimming_pool": 0.0,
  "state_of_building": "GOOD",
  "main_city": "brussel",
  "province": "brussel"
}
```




## Project timeline
The project was carried out within the framework of Data&AI training by [BeCode](https://becode.org/) within 5 days.
- Day 1-2 learning Fast API documentation
- Day 3 creation of the API
- Day 4 deployment of the API using Docker on Render
- Day 5 structuring


## Authors
The program was developed by [Alfiya Khabibullina](https://github.com/justalphie) under the supervision of the coach [Vanessa Rivera-Quinones](https://github.com/vriveraq)
