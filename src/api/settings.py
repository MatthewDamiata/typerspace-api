class InfoMsgs:
    authorized_user = "User logged in with name: {name} and email: {email}."
    unsuccessful_login = "User attempted login but failed."
    user_already_in_db = "User [{name}, {email}] already exists in DB."
    user_added_to_db = "User [{name}, {email}] added to DB."
    transcribed_video = "Video with ID: {video_id} transcribed."
    transcribed_video_error = (
        "Error transcribing video with ID: {video_id}. Error: {error}."
    )
    couldnt_find_caption = "Couldn't find caption for video with ID: {video_id}."
    sanitizing_video = "Sanitizing transcript for video with ID: {video_id}."
    getting_transcription_list = "Getting transcription list for video with ID: {video_id}."
    
class LanguageEnum:
    ENGLISH = "English"