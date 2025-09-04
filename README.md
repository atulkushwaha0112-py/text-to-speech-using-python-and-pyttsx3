# text-to-speech-using-python-and-pyttsx3
pyttsx3 is a Python library that converts text into spoken words using Windows' built-in voice engine. It works offline and lets you control voice, rate, and volume.

<!--🧠 Highlight.js and Font Awesome already included in your Blogger theme-->
<!--🧠 Highlight.js for Code Highlighting-->
<link href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css" rel="stylesheet"></link>

<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet"></link>
<h2>🎙️ Text-to-Speech (TTS) in Python using <code>pyttsx3</code> for Windows</h2>

  <!-- WhatsApp Channel Promo (Theme-Compatible) -->
<ul style="list-style: none; padding-left: 0; margin-top: 10px; margin-bottom: 20px; font-family: Arial, sans-serif;">
  <li style="margin: 8px 0; font-size: 18px;">
    <i class="fab fa-whatsapp" style="margin-right: 10px;"></i>
    <a href="https://whatsapp.com/channel/0029Vb5oq3gBA1f23Latsb3a" target="_blank" style="text-decoration: none;">
      📢 Stay updated with tutorials, projects & coding hacks — <strong>Join our WhatsApp Channel</strong>
    </a>
  </li>
</ul>


<p>
<code>pyttsx3</code> is a Python library that converts text into spoken words using Windows' built-in voice engine. It works offline and lets you control voice, rate, and volume.
</p>

<h3>🔧 Step 1: Install pyttsx3</h3>
<pre><code class="language-bash">pip install pyttsx3</code></pre>

<h3>🧠 Step 2: Basic Example</h3>
<pre><code class="language-python">
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, welcome to pyttsx3 text to speech!")
engine.runAndWait()
</code></pre>

<h3>💡 Step 3: List All Supported Voices</h3>
<pre><code class="language-python">
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for idx, voice in enumerate(voices):
    print(f"{idx}. Name: {voice.name}, ID: {voice.id}, Lang: {voice.languages}")
</code></pre>

<p>
You’ll typically see voices like:
</p>
<pre><code class="language-text">
0. David - English (US) - Male
1. Zira - English (US) - Female
</code></pre>

<h3>🎙️ Change Voice: Male / Female</h3>
<pre><code class="language-python">
engine.setProperty('voice', voices[0].id)  # Male
engine.setProperty('voice', voices[1].id)  # Female
Note - It support only two Types of Voices But you can change Pitch
</code></pre>

<h3>⚙️ Set Rate, Volume, and Speak</h3>
<pre><code class="language-python">
engine.setProperty('rate', 150)    # Default ~200
engine.setProperty('volume', 1.0)  # Range: 0.0 to 1.0

engine.say("This is a custom voice with speed and volume.")
engine.runAndWait()
</code></pre>

<h3>🌐 Supported Languages</h3>
<p>
<code>pyttsx3</code> uses system-installed voices. You can add new voices in Windows:
</p>
<h2>🗣️ How to Install More Text-to-Speech Voices in Windows (for pyttsx3)</h2>

<p>If you want more voices like <strong>Hindi, Spanish, French, or regional English (India/UK/US)</strong> in your <code>pyttsx3</code> project, follow these easy steps:</p>

<h3>✅ Step-by-Step Guide</h3>

<ol>
  <li>🛠️ Open <strong>Settings</strong> → Press <code>Win + I</code></li>
  <li>⏳ Go to <strong>Time &amp; Language &gt; Speech</strong></li>
  <li>🧩 Scroll down to <strong>Manage Voices</strong> (in Windows 11)</li>
  <li>➕ Click <strong>Add voices</strong></li>
  <li>🌐 Choose from languages like:
    <ul>
      <li>✅ <strong>English (India)</strong></li>
      <li>✅ <strong>Hindi</strong></li>
      <li>✅ <strong>Spanish</strong>, <strong>French</strong>, etc.</li>
    </ul>
  </li>
  <li>⬇️ Wait for the download to finish</li>
  <li>🔁 <strong>Restart your PC</strong> to activate new voices</li>
</ol>

<h3>💻 Python Code: List All Installed Voices</h3>
<pre><code class="language-python">
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for idx, voice in enumerate(voices):
    print(f"{idx}. Name: {voice.name}, ID: {voice.id}, Lang: {voice.languages}")
</code></pre>

<h3>🎯 Example Output:</h3>
<pre><code class="language-text">
0. Microsoft David Desktop - English (US)
1. Microsoft Zira Desktop - English (US)
2. Microsoft Ravi - English (India)
3. Microsoft Heera - Hindi
4. Microsoft Helena - Spanish (Spain)
</code></pre>

<h3>🧠 How to Use a Specific Voice (by Index or Language)</h3>

<p>👉 Using voice by index:</p>
<pre><code class="language-python">
engine.setProperty('voice', voices[2].id)  # Ravi - English (India)
</code></pre>

<p>👉 Auto-select by language (e.g., Hindi):</p>
<pre><code class="language-python">
for voice in voices:
    if 'hi-IN' in voice.languages or 'Hindi' in voice.name:
        engine.setProperty('voice', voice.id)
        break
</code></pre>

<h3>💡 Tips</h3>
<ul>
  <li><i class="fas fa-bolt"></i> Use <code>voice.languages</code> to detect language codes like <code>'en-IN'</code>, <code>'hi-IN'</code>, <code>'es-ES'</code></li>
  <li><i class="fas fa-tools"></i> Voices must be installed via Windows Settings first</li>
  <li><i class="fas fa-sync-alt"></i> Always restart after installing new voices</li>
</ul>

<h3>🎙️ Save Voice Output as MP3 (Optional)</h3>
<pre><code class="language-python">
engine.save_to_file("यह आवाज़ फाइल में सेव होगी", "output.mp3")
engine.runAndWait()
</code></pre>

<h3>📌 Conclusion</h3>
<p>Using <code>pyttsx3</code> with Windows' built-in and custom-installed voices lets you create advanced text-to-speech apps in multiple languages — <strong>fully offline!</strong></p>











<h3>📂 Full Project Example</h3>
<pre><code class="language-python">
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female

engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)

text = "Hello! This is a text-to-speech demo using pyttsx3 on Windows."
engine.say(text)
engine.runAndWait()
</code></pre>

<h3>🧠 Tricks &amp; Hacks</h3>
<ul>
  <li><i class="fas fa-magic"></i> Use <code>engine.save_to_file("Text", "output.mp3")</code> to save TTS as audio file.</li>
  <li><i class="fas fa-language"></i> Install more Windows voices for different languages.</li>
  <li><i class="fas fa-cogs"></i> Create a voice menu in your app for switching between voices live.</li>
</ul>

<h3>❓ FAQ</h3>
<p><strong>Q. Does pyttsx3 work offline?</strong><br />✅ Yes, it is fully offline as it uses built-in TTS engines.</p>
<p><strong>Q. Can I change the language?</strong><br />✅ Yes, if that language's voice is installed on your Windows system.</p>
<p><strong>Q. How to slow down the voice?</strong><br />🎚️ Use <code>engine.setProperty('rate', 120)</code></p>

<h3>📦 Extra Tip: Save to MP3 File</h3>
<pre><code class="language-python">
engine.save_to_file("Save this text to file", "speech.mp3")
engine.runAndWait()
</code></pre>

<h2>🎯 Conclusion</h2>
<p>
<code>pyttsx3</code> is a powerful and flexible offline TTS library for Python developers on Windows. Customize voices, export audio, and even integrate it in GUIs or games!
</p>
