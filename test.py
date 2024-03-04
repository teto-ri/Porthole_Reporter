import requests
import pandas as pd

ACCIDENT_DATA_URL = "http://waterboom.iptime.org:1101/get-locations"

def fetch_and_format_accident_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # 실제 데이터를 JSON 형태로 변환
            data = response.json()
            # JSON 데이터를 DataFrame으로 변환
            accidents_df = pd.DataFrame(data)
            # 샘플 데이터 형식에 맞추어 컬럼 변환
            formatted_df = pd.DataFrame({
                'user_id': accidents_df['userId'],
                'id' : accidents_df['id'],
                'type': accidents_df['progress'],
                'category': accidents_df['type'],  
                'date': pd.to_datetime(accidents_df['time'],format='mixed'),  # 'time'을 datetime 형식으로 변환
                'district': accidents_df['area2'],  # 'district'는 'area2' 값 사용
                'description': accidents_df['type'],  # 'description'은 'type' 값 사용
                'detail_location': accidents_df['road'],
                'location': list(zip(accidents_df['latitude'], accidents_df['longitude']))  # 'location'은 'latitude'와 'longitude'를 튜플로 묶음
            })
            return formatted_df
        else:
            return pd.DataFrame()
    except Exception as e:
        print(e)
        return pd.DataFrame()
    
accidents = fetch_and_format_accident_data(ACCIDENT_DATA_URL)
print(accidents)