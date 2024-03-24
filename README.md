# Flight Delay Predictor

### Input
![Screenshot 2024-03-24 at 4 42 59 PM](https://github.com/adil200/Flight-Delay-Prediction/assets/75264739/b4e7f4e6-f80a-4ffd-a3d6-2fa3e2451654)
### Output
![Screenshot 2024-03-24 at 4 43 06 PM](https://github.com/adil200/Flight-Delay-Prediction/assets/75264739/0b47c23e-7c02-4d55-87ca-92e26908324d)


## Description

The Flight Delay Predictor is a sophisticated tool designed to assist airlines and travelers in anticipating flight delays. By leveraging machine learning algorithms and historical flight data, the predictor accurately forecasts the likelihood of flight delays, empowering airlines to optimize their operations and travelers to plan their journeys more efficiently. With a user-friendly interface and real-time prediction capabilities, this project aims to enhance the overall travel experience by minimizing the impact of unexpected delays.

## Features

-   Input fields for air time and distance to predict flight delays.
-   Real-time prediction based on machine learning models.
-   Intuitive web interface accessible from various devices.

## Warning Note

Please note that while the Flight Delay Predictor provides valuable insights into potential flight delays, it should not be used as the sole basis for travel decisions. Factors such as weather conditions, air traffic control, and other unforeseen circumstances may impact flight schedules. Always refer to official airline notifications and consult with travel professionals for the most accurate information.

## Installation

### Prerequisites

-   Python 3.8 or higher
-   Flask

### Setup

1.  Clone the repository and navigate to the directory.
    
2.  Install the required Python dependencies:
    

```bash
pip install -r requirements.txt
```

3.  Extract the `flight_delay_predict.csv.zip` file into the project directory.
    
4.  Open a Terminal or Command Prompt and run the Flask server:
    

```bash
flask run
```

5.  Open [http://127.0.0.1:5000](http://127.0.0.1:5000/) in the browser to access the web app.

## Usage

1.  Access the web application through your browser.
2.  Enter the air time and distance of your flight into the provided input fields.
3.  Submit the information to receive a prediction of potential flight delays.
4.  The prediction result will be displayed on the screen, indicating the likelihood of delays and any recommended actions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

-   The Flight Delay Predictor project was developed to address the challenges faced by airlines and travelers in predicting and managing flight delays effectively. Special thanks to the team for their contributions and support in making this project possible.
