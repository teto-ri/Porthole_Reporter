from init_data import status_class, status_description


def make_popup(accident):
    popup_html = f"""
                <div>
                    <style>
                        .status-indicator {{
                            height: 10px;
                            width: 10px;
                            background-color: #bbb;
                            border-radius: 50%;
                            display: inline-block;
                        }}
                        .status-complete {{ background-color: #4CAF50; }} /* Green */
                        .status-hold {{ background-color: #FFEB3B; }} /* Yellow */
                        .status-pending {{ background-color: #F44336; }} /* Red */
                    </style>
                </div>
                    <span class="status-indicator {status_class[accident['type']]}"></span>
                    <span class="status-description">{status_description[accident['type']]}</span>
                    <span class="accident-id">- id : {accident['id']}</span>
                <div style="font-family: Arial; text-align: center;">
                    <h4>종류 : {accident['category']}</h4>
                    <hr style="margin: 1px;">
                    <p><strong>신고날짜:</strong> {accident['date'].strftime('%Y-%m-%d %H:%M:%S')}</p>
                    <p><strong>신고자:</strong> {accident['user_id']}</p>
                    <p><strong>시군구:</strong> {accident['district']}</p>
                    <p><strong>설명:</strong> {accident['description']}</p>
                    <p><strong>위치:</strong> {accident['detail_location']}</p>
                    <div>
                        <style>
                            .complete-button {{
                                padding: 10px 15px;
                                background-color: #4CAF50; /* Green */
                                color: white;
                                border: none;
                                border-radius: 5px;
                                cursor: pointer;
                                font-family: Arial;
                                margin-right: 5px; /* Add some space between the buttons */
                            }}

                            .hold-button {{
                                padding: 10px 15px;
                                background-color: #FF9800; /* Orange */
                                color: white;
                                border: none;
                                border-radius: 5px;
                                cursor: pointer;
                                font-family: Arial;
                                margin-right: 5px;
                            }}
                            
                            .delete-button {{
                                padding: 10px 15px;
                                background-color: #E34234; /* Red */
                                color: white;
                                border: none;
                                border-radius: 5px;
                                cursor: pointer;
                                font-family: Arial;
                            }}
                            
                            .complete-button:hover, .hold-button:hover, .delete-button:hover {{
                                opacity: 0.8;
                            }}
                            
                            .complete-button:active, .hold-button:active, .delete-button:active {{
                                opacity: 0.6;
                            }}
                            
                            .button-icon {{
                                padding-right: 5px;
                            }}
                        </style>

                        <button class="complete-button" onclick="sendGetRequest({accident['id']},'finished'); alert('완료 처리되었습니다.');">
                            <span class="button-icon">&#10004;</span> 완료
                        </button>
                        
                        <button class="hold-button" onclick="sendGetRequest({accident['id']},'checked');  alert('확인 처리되었습니다.');">
                            <span class="button-icon">&#9888;</span> 확인
                        </button>
                        
                        <button class="delete-button" onclick="removeGetRequest({accident['id']});  alert('삭제 처리되었습니다.');">
                            <span class="button-icon">&#128465;</span> 삭제
                        </button>
                        
                        <script>
                        function sendGetRequest(id, progress) {{
                            const url = `http://waterboom.iptime.org:1101/update-location-progress?id=${{id}}&progress=${{progress}}`;

                            fetch(url)
                            .then(response => {{
                                if (!response.ok) {{
                                    throw new Error('Network response was not ok ' + response.statusText);
                                }}
                                return response.json();
                            }})
                            .then(data => {{
                                console.log('Success:', data);
                                // Handle success here
                            }})
                            .catch((error) => {{
                                console.error('Error:', error);
                                // Handle errors here
                            }});
                        }}
                        function removeGetRequest(id) {{
                            const url = `http://waterboom.iptime.org:1101/delete-location?id=${{id}}`;

                            fetch(url)
                            .then(response => {{
                                if (!response.ok) {{
                                    throw new Error('Network response was not ok ' + response.statusText);
                                }}
                                return response.json();
                            }})
                            .then(data => {{
                                console.log('Success:', data);
                                // Handle success here
                            }})
                            .catch((error) => {{
                                console.error('Error:', error);
                                // Handle errors here
                            }});
                        }}
                        </script>
                    </div>
                """
    return popup_html
