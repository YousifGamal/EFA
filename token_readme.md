## How to use tokens
- Put @token_required decorater before route function for example at line 349 in app.py in update Profile route 
- In the front you need to login inorder to receive a token which is stored in local storage window
- To make an axios request you need to put the token in header for token_required routes as in updateProfile.vue line `254` for get requests and line `205` for put and post requests. 
- username , id , role , token are stored in the local storage so to access any one write `localStorage.getItem("token"),`
- Any questions or inquires please contact me on `khaledgala002@gmail.com` reply within 24 hours.