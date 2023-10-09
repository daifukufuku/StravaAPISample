import requests
import time

url = "https://www.strava.com/api/v3/athlete/activities"
headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
}
params = {
    'after': UNIX_TIME_STAMP, # Fetch activities after this timestamp
}

response = requests.get(url, headers=headers, params=params)

# Print results on successful request
if response.status_code == 200:
    data = response.json()
    
    # Retrieve activity data
    for activity in data:
        id = activity.get('id')
        name = activity.get('name')
        distance = activity.get('distance')
        moving_time = activity.get('moving_time')
        activity_type = activity.get('type')
        start_date = activity.get('start_date')
    
        print(f"ID: {id}")
        print(f"Title: {name}")
        print(f"Distance: {distance} m")
        print(f"Duration: {moving_time} seconds")
        print(f"Type: {activity_type}")
        print(f"Start Time: {start_date}")
        print("-" * 50)
        
        # Retrieve details for each activity
        activity_url = f"https://www.strava.com/api/v3/activities/{id}"
        activity_response = requests.get(activity_url, headers=headers)
        if activity_response.status_code == 200:
            activity_data = activity_response.json()
            
            # Display detailed activity info
            description = activity_data.get('description', '')
            calories = activity_data.get('calories', '')
            perceived_exertion = activity_data.get('perceived_exertion', '')
            
            print(f"Description: {description}")
            print(f"Calories: {calories}")
            print(f"Perceived Exertion: {perceived_exertion}")
            print("-" * 50)

            # Display information for each split
            splits_metric = activity_data.get('splits_metric', [])
            for split in splits_metric:
                split_distance = split.get('distance', '')
                elapsed_time = split.get('elapsed_time', '')
                moving_time = split.get('moving_time', '')
                average_speed = split.get('average_speed', '')
                average_heartrate = split.get('average_heartrate', '')
                
                print(f"Split Distance: {split_distance} m")
                print(f"Elapsed Time: {elapsed_time} seconds")
                print(f"Moving Time: {moving_time} seconds")
                print(f"Average Speed: {average_speed} m/s")
                print(f"Average Heart Rate: {average_heartrate} bpm")
                print("===============================================")
        
        # Delay to prevent rapid-fire requests
        time.sleep(2)
