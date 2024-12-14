 <h1>🌦️ Umbrella Reminder Bot</h1>
    <p>
        This Python-based project is a <strong>weather reminder bot</strong> that keeps you informed about the weather in your city and sends timely notifications to ensure you're prepared—whether it's sunny skies or a rainy day! 🌂
    </p>

<h2>⚙️ Features</h2>
    <ul>
        <li><strong>Weather Updates:</strong> Fetches real-time weather data for your city.</li>
        <li><strong>WhatsApp Notifications:</strong> Sends weather updates via WhatsApp messages. ✅</li>
        <li><strong>Email Notifications:</strong> (Currently Buggy 🚧) Emails the weather updates, but encounters an authentication error.</li>
        <li><strong>Daily Scheduling:</strong> Automatically schedules weather reminders at a time of your choice using <code>schedule</code>.</li>
    </ul>

<h2>🐛 Known Issues</h2>
    <p>
        <strong>Email Notification Fails:</strong> The <code>umbrella_reminder()</code> function currently raises an error:  
        <code>❌ Authentication error: Check your email or app password settings.</code>  
        The code may need better handling of SMTP authentication or App Password integration.
    </p>

<h2>🚀 How to Run the Code</h2>
    <ol>
        <li><strong>Clone the Repository:</strong>
            <pre><code>
git clone https://github.com/&lt;Dark-Programer&gt;/umbrella-reminder-bot.git
cd umbrella-reminder-bot
            </code></pre>
        </li>
        <li><strong>Install Dependencies:</strong>
            <pre><code>
pip install -r requirements.txt
            </code></pre>
        </li>
        <li><strong>Run the Script:</strong>
            <pre><code>
python weather_reminder.py
            </code></pre>
        </li>
        <li><strong>Provide User Inputs:</strong>
            <ul>
                <li>City Name</li>
                <li>Email & Password (for email notifications)</li>
                <li>Time (in 24-hour format)</li>
                <li>Phone Number (with country code for WhatsApp)</li>
            </ul>
        </li>
    </ol>

<h2>📋 Requirements</h2>
    <ul>
        <li>Python 3.7+</li>
        <li>Libraries: <code>schedule</code>, <code>smtplib</code>, <code>requests</code>, <code>beautifulsoup4</code>, <code>pywhatkit</code></li>
    </ul>

<h2>🛠️ Contributions Welcome!</h2>
    <p>
        If you're a developer looking to fix or improve the project, feel free to:
        <ul>
            <li>Submit a Pull Request</li>
            <li>Open an Issue for discussion</li>
        </ul>
    </p>
    <p><strong>Focus Area:</strong> Fixing the email notification functionality to resolve authentication issues.</p>

<h2>📝 Note</h2>
    <ul>
        <li><strong>WhatsApp Integration:</strong> Works seamlessly. Messages are delivered as scheduled.</li>
        <li><strong>Email Notification:</strong> Currently failing due to SMTP authentication errors. Please review the <code>umbrella_reminder()</code> function for potential fixes.</li>
    </ul>

<h2>📧 Contact</h2>
    <p>
        Feel free to reach out if you have suggestions or encounter any issues:
        <ul>
            <li><strong>GitHub Issues:</strong> Submit <a href="https://github.com/Dark-Programer/umbrella-remainder-bot/issues">here</a>.</li>
        </ul>
    </p>