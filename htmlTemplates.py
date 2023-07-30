css = '''
<style>
    .stTextInput input {
        border: 1px solid #ced4da;
        border-radius: 0.25rem;
        color: #495057;
        padding: 0.375rem 0.75rem;
        line-height: 1.5;
        font-size: 1rem;
    }

    /* Style the text output box */
    .stMarkdown {
        border: 1px solid #ced4da;
        border-radius: 0.25rem;
        color: #495057;
        padding: 0.375rem 0.75rem;
        line-height: 1.5;
        font-size: 1rem;
        background-color: #f8f9fa;
    }
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="eaglebot.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="eaglebot.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''