# Mr. Rudra

Mr. Rudra is a versatile and advanced AI-powered assistant available in two versions:

1. **Rudra_Assistant**: OpenAI-based, providing faster performance and streaming capabilities (for users with OpenAI API access).
2. **Rudra_Cheap**: A cost-effective version leveraging free methods for assistant development.

Rudra is a multi-modal assistant integrating Gemini, Groq, and ElevenLabs models. It is both conversational and utility-based, capable of:
- Taking screenshots
- Capturing webcam images
- Extracting clipboard content
- Analyzing provided inputs

With back-and-forth communication and memory capabilities, Rudra ensures engaging and dynamic user interactions.

## Models

1. **Groq_Whisper ( distil-whisper-large-v3-en )**:
   - Groq's whisper model for SST (Speech-to-Text).
   - Note: The multilingual model occasionally misinterprets English as Russian due to accent nuances.

2. **Groq_LLM ( gemma2-9b-it )**:
   - Groq's LLM model for text generation and intent extraction.
   - Determines user intent from input (e.g., "extract clipboard," "take screenshot," "capture webcam," or "None").
   - Also used for explaining visual inputs like screenshots and webcam captures.

3. **genai ( gemini-1.5-flash-latest )**:
   - A vision analysis model extracting semantic meanings from images to provide context.
   - Processes image data to create contextually relevant responses.

4. **ElevenLabs ( eleven_multilingual_v2 )**:
   - A Text-to-Speech (TTS) model for converting responses into speech.
   - Uses the voice "Adam" to match Rudra's masculine persona.
   - Provides a number of voices with its voice id to choose from: [Voices List](./elabs_voices.txt) 

5. **OpenAI ( tts-1 )**:
   - A Text-to-Speech (TTS) model for converting responses into speech. Offers Streaming methods.
   - Uses the voice "Onyx" to match Rudra's masculine persona.
   - OpenAI tts service provides 6 different voices to choose from *['shimer' , 'nova' , 'onyx' , 'fable, 'echo' , 'alloy' ]*

### Required APIs
* GROQ_API_TOKEN
* Gemini_API_TOKEN
* ElevenLab_API_TOKEN
* OpenAI_API_TOKEN (Optional)


## Key Features

1. **Multi-Model Integration**: Combines four specialized models to deliver advanced capabilities.
2. **Utility-Based Tasks**: Beyond conversations, Rudra performs utility tasks like clipboard extraction and webcam imaging.
3. **Wake Word Activation**: Responds only to the designated wake word for focused interaction.
4. **Memory Capabilities**: Tracks input history to provide context-aware responses.
5. **Conversational Proficiency**: Facilitates natural, engaging, and full-fledged conversations.
6. **Task-Specific Prompts**: Each model operates with detailed prompts for precision and accuracy.

## Steps  
Here are steps of the order of functiona calling that takes place
1. start_listening()
2. callback(recognizer, audio)
3. wav_to_text(audio_path)
4. extract_prompt( transcribed_text, wake_word )
5. function_call(prompt)
6. take_screenshot() | web_cam_capture() | get_clipboard_text()
7. vision_prompt(prompt, photo_path)
8. groq_prompt(prompt, img_context)
9. speak(response)

## Working

1. **Voice Detection and Callback**:
   - Starts a loop listening mechanism to detect voice input.
   - Triggers a callback function upon detecting audio, where main activities occur.

2. **Audio Processing**:
   - Detected audio is saved as a file (*prompt.wav*).
   - Transcribed using SST to generate a textual representation of the user's voice input.

3. **Prompt Extraction**:
   - Removes the wake word to create a clean prompt.
   - Defaults to "Hi" if no wake word is detected (adjustable for performance).

4. **Intent Extraction**:
   - Determines user intent (e.g., "extract clipboard," "take screenshot," etc.).

5. **Task Execution**:
   - Executes the required task based on the extracted intent.
   - Processes visual inputs (if any) for semantic meaning using the vision analysis model.

6. **Response Generation**:
   - Combines clean prompts and image context (if available) to generate a response.
   - Prints the response to the screen and converts it to speech using TTS.

### Setting Up

To talk to Mr. Rudra, make sure to create a virtual environment and install the dependencies.
```
pip install -r requirements.txt
```
If you have OpenAI API, rudra_assistant will be fast and smart choice for you, if not the cost effective rudra will be a better choice.

### Conclusion
Rudra combines advanced AI capabilities with practical utility, ensuring a seamless and efficient user experience.
Happy Talking
