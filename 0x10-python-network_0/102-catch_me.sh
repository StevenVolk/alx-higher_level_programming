#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me and responds You got me!
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: School" -d "user_id=98"
