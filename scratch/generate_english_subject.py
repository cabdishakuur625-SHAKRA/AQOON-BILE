import json
import re
import os

def create_ch1_questions():
    # Chapter 1: Unit 1 & 2 (Never Forget & Oral Presentation)
    # Focus: Memory, Poetry, Rhyme, Syllables, Intonation, Oral Presentations, Public Speaking, Present Simple vs Past Simple.
    easy = [
        {"q": "What is the primary theme of the poem 'Never Forget' in Unit 1?", "opts": {"a": "The inevitability of death, justice, and the Day of Judgment", "b": "The beauty of nature and wildlife", "c": "Modern technology and computers", "d": "The process of building colossal houses"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'write'?", "opts": {"a": "right", "b": "rite", "c": "rate", "d": "rot"}, "ans": "a"},
        {"q": "Which word is stressed in the sentence: 'I wrote the love letter for YOU' (implying not for someone else)?", "opts": {"a": "I", "b": "wrote", "c": "letter", "d": "YOU"}, "ans": "d"},
        {"q": "What type of intonation is typically used for a Wh-question like 'Where is my father?'", "opts": {"a": "Falling intonation", "b": "Rising intonation", "c": "Flat intonation", "d": "Rising-falling intonation"}, "ans": "a"},
        {"q": "What type of intonation is typically used for yes/no questions like 'Is it cold?'", "opts": {"a": "Rising intonation", "b": "Falling intonation", "c": "Flat intonation", "d": "No intonation"}, "ans": "a"},
        {"q": "In a poem, the pattern of rhymes at the end of each line is called the:", "opts": {"a": "rhyme scheme", "b": "rhythm meter", "c": "alliteration", "d": "stanza structure"}, "ans": "a"},
        {"q": "Identify the homophone for the word 'back'.", "opts": {"a": "bake", "b": "bark", "c": "back (there is no homophone listed)", "d": "beck"}, "ans": "c"},
        {"q": "Which of the following refers to a talk giving information about a product or idea to an audience?", "opts": {"a": "Oral presentation", "b": "Silent reading", "c": "Private diary", "d": "Internal monologue"}, "ans": "a"},
        {"q": "What is the synonym of the word 'deception'?", "opts": {"a": "honesty", "b": "dishonesty or misleading behavior", "c": "clarity", "d": "generosity"}, "ans": "b"},
        {"q": "What is the antonym of the word 'never'?", "opts": {"a": "always", "b": "sometimes", "c": "rarely", "d": "seldom"}, "ans": "a"},
        {"q": "Which of the following is the past tense of 'forget'?", "opts": {"a": "forgot", "b": "forgotten", "c": "forgetting", "d": "forgets"}, "ans": "a"},
        {"q": "In public speaking, maintaining eye contact with the audience helps to:", "opts": {"a": "build rapport and engagement", "b": "distract the listeners", "c": "read notes hidden on the floor", "d": "intimidate the crowd"}, "ans": "a"},
        {"q": "Which pronoun is a first-person singular pronoun?", "opts": {"a": "I", "b": "you", "c": "he", "d": "they"}, "ans": "a"},
        {"q": "Complete: Yesterday, we _____ a beautiful poem in the English class.", "opts": {"a": "read", "b": "reads", "c": "reading", "d": "are reading"}, "ans": "a"},
        {"q": "What do we call a division of a poem consisting of a series of lines?", "opts": {"a": "Stanza", "b": "Paragraph", "c": "Sentence", "d": "Chapter"}, "ans": "a"},
        {"q": "Which sound device is the repetition of consonant sounds at the beginning of words?", "opts": {"a": "Alliteration", "b": "Assonance", "c": "Onomatopoeia", "d": "Rhyme"}, "ans": "a"},
        {"q": "When giving a speech, if you speak too fast, your audience might:", "opts": {"a": "struggle to understand you", "b": "applaud your speed", "c": "fall asleep immediately", "d": "hear you better"}, "ans": "a"},
        {"q": "What is the base form of the verb 'judged'?", "opts": {"a": "judge", "b": "judging", "c": "judgment", "d": "judges"}, "ans": "a"},
        {"q": "Which of the following is a homophone of the word 'hear'?", "opts": {"a": "here", "b": "hair", "c": "hare", "d": "her"}, "ans": "a"},
        {"q": "Complete: An oral presentation should always start with a brief _____.", "opts": {"a": "introduction", "b": "conclusion", "c": "applause", "d": "questionnaire"}, "ans": "a"},
        {"q": "Which word has a positive connotation related to public speaking?", "opts": {"a": "confident", "b": "nervous", "c": "monotone", "d": "unprepared"}, "ans": "a"},
        {"q": "Identify the noun form of the verb 'present'.", "opts": {"a": "presentation", "b": "presently", "c": "presenting", "d": "presented"}, "ans": "a"},
        {"q": "Which of these is a non-verbal communication tool?", "opts": {"a": "Body language and gestures", "b": "Speaking loudly", "c": "Reading a script", "d": "Using a microphone"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "In the poem 'Never Forget', what does the phrase 'blood on your hands' symbolize?", "opts": {"a": "Literal injury from farming", "b": "Guilt and responsibility for wrongdoing or murder", "c": "Painting with red colors", "d": "Working hard in a medical clinic"}, "ans": "b"},
        {"q": "How does 'rising intonation' function in tag questions like 'They will come tomorrow, won't they?' when seeking confirmation?", "opts": {"a": "It indicates uncertainty and asks a genuine question", "b": "It indicates absolute certainty", "c": "It shows that the speaker is angry", "d": "It marks the end of a speech"}, "ans": "a"},
        {"q": "Which statement best describes the role of 'stress' in spoken English sentences?", "opts": {"a": "It is only used to show that the speaker is under pressure", "b": "It highlights key content words to clarify the intended meaning of the speaker", "c": "It requires shouting at the end of each word", "d": "It makes all syllables sound exactly the same length"}, "ans": "b"},
        {"q": "What is the term for two words that are spelled differently and have different meanings, but are pronounced the same?", "opts": {"a": "Homophones", "b": "Synonyms", "c": "Antonyms", "d": "Homographs"}, "ans": "a"},
        {"q": "In the sentence 'I wrote the LOVE letter for you' (with stress on love), what is the implied meaning?", "opts": {"a": "I wrote a love letter, not a business or ordinary letter", "b": "I did not write the letter myself", "c": "I wrote the letter for someone else", "d": "I hate writing letters"}, "ans": "a"},
        {"q": "What is the synonym of the word 'tainted' as used in 'tainted with deception'?", "opts": {"a": "purified", "b": "polluted or corrupted", "c": "strengthened", "d": "decorated"}, "ans": "b"},
        {"q": "In an oral presentation, what is the purpose of the 'body' section?", "opts": {"a": "To introduce the speaker's background", "b": "To explain the main points in detail with evidence", "c": "To thank the audience for listening", "d": "To ask the audience for feedback"}, "ans": "b"},
        {"q": "Complete the sentence: If you want to deliver a memorable presentation, you _____ practice multiple times beforehand.", "opts": {"a": "should", "b": "might", "c": "would", "d": "shall"}, "ans": "a"},
        {"q": "Which word is the antonym of 'justice'?", "opts": {"a": "injustice", "b": "fairness", "c": "equity", "d": "lawfulness"}, "ans": "a"},
        {"q": "What is the sound pattern where vowel sounds are repeated within words close to each other?", "opts": {"a": "Assonance", "b": "Alliteration", "c": "Rhyme", "d": "Onomatopoeia"}, "ans": "a"},
        {"q": "Which sentence is written in the passive voice?", "opts": {"a": "The poem was recited beautifully by the student.", "b": "The student recited the poem beautifully.", "c": "The student is reciting a new poem.", "d": "The student forget the poem lines."}, "ans": "a"},
        {"q": "What is the past participle form of the verb 'write'?", "opts": {"a": "written", "b": "wrote", "c": "writes", "d": "writing"}, "ans": "a"},
        {"q": "When planning an oral presentation, what does analyzing your 'audience' involve?", "opts": {"a": "Finding out their age, interest, and prior knowledge of the topic", "b": "Counting the exact number of chairs in the room", "c": "Designing complex slides with animations", "d": "Buying handouts and books for them"}, "ans": "a"},
        {"q": "Identify the conjunction in the sentence: 'He was nervous, yet he delivered a powerful presentation.'", "opts": {"a": "yet", "b": "was", "c": "nervous", "d": "delivered"}, "ans": "a"},
        {"q": "What does a falling intonation usually suggest at the end of a declarative sentence?", "opts": {"a": "Completeness and finality of statement", "b": "A question requiring a yes/no answer", "c": "Hesitation or doubt", "d": "An interruption by another speaker"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'road'?", "opts": {"a": "rode", "b": "rod", "c": "rid", "d": "red"}, "ans": "a"},
        {"q": "What spelling rule applies when adding '-ing' to the verb 'forget'?", "opts": {"a": "Double the final consonant 't' (forgetting)", "b": "Drop the final letter 't'", "c": "Change 'e' to 'y'", "d": "Keep spelling same (forgeting)"}, "ans": "a"},
        {"q": "In public speaking, 'intonation' refers to:", "opts": {"a": "the rise and fall of the voice pitch in speaking", "b": "speaking with a loud volume", "c": "avoiding eye contact with the audience", "d": "reading from a slide word-for-word"}, "ans": "a"},
        {"q": "Which of these transitions is best used to introduce a concluding statement in a speech?", "opts": {"a": "In conclusion", "b": "Furthermore", "c": "First of all", "d": "For example"}, "ans": "a"},
        {"q": "What is the primary purpose of visual aids in a presentation?", "opts": {"a": "To support and clarify the speaker's spoken points", "b": "To replace the speaker completely", "c": "To show colorful unrelated pictures", "d": "To list the entire text of the speech"}, "ans": "a"},
        {"q": "Identify the pronoun in: 'She gave them her book.'", "opts": {"a": "She", "b": "gave", "c": "book", "d": "her (adjective in this case)"}, "ans": "a"},
        {"q": "What is the meaning of the prefix 'de-' in words like 'deception' or 'decrease'?", "opts": {"a": "down, away from, or reversing", "b": "again or repeat", "c": "before or early", "d": "excessive or high"}, "ans": "a"},
        {"q": "Which word is a synonym of 'campaign' in the context of campaigning for change?", "opts": {"a": "advocate or crusade", "b": "halt", "c": "forget", "d": "oppose"}, "ans": "a"},
        {"q": "Complete: By the time the presentation started, the speaker _____ his notes.", "opts": {"a": "had reviewed", "b": "reviews", "c": "will review", "d": "is reviewing"}, "ans": "a"},
        {"q": "Which word is a homophone of the word 'soul'?", "opts": {"a": "sole", "b": "soil", "c": "sale", "d": "seal"}, "ans": "a"},
        {"q": "What is the main advantage of practicing a speech in front of a mirror?", "opts": {"a": "It helps monitor body language, posture, and facial expressions", "b": "It eliminates the need for notes entirely", "c": "It changes the speaker's vocal range", "d": "It improves the microphone setup"}, "ans": "a"},
        {"q": "In the sentence 'I WROTE the love letter for you' (stressing wrote), what is implied?", "opts": {"a": "I wrote it (did not type it or buy it)", "b": "Someone else wrote the letter", "c": "It was not a love letter", "d": "The letter was for someone else"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "In poetry analysis, which of the following is defined as a foot consisting of an unstressed syllable followed by a stressed syllable?", "opts": {"a": "Iamb", "b": "Trochee", "c": "Anapest", "d": "Dactyl"}, "ans": "a"},
        {"q": "Analyze the intonation: A speaker says 'You are coming, aren't you?' with a falling tone on the tag. This implies that the speaker:", "opts": {"a": "expects the listener to agree and is not really asking a question", "b": "is highly unsure and asking for information", "c": "is surprised that the listener is coming", "d": "does not want the listener to come"}, "ans": "a"},
        {"q": "How does shifting the stress to the word 'I' in 'I wrote the love letter for you' alter the semantic implication?", "opts": {"a": "It implies that I (and no one else) wrote the letter", "b": "It emphasizes the action of writing", "c": "It highlights the romantic nature of the letter", "d": "It asserts the identity of the recipient"}, "ans": "a"},
        {"q": "Which sound device is employed in the line: 'Those who can't bribe are forced to walkthrough a thorn thicket'?", "opts": {"a": "Alliteration of the 'th' sound", "b": "Assonance of the 'o' sound", "c": "Onomatopoeia of the forest", "d": "End rhyme with thicket"}, "ans": "a"},
        {"q": "What is the meaning of the word 'pointless' in: 'Here justice is as pointless as a poorly-tied camel-halter'?", "opts": {"a": "futile, ineffective, or lacking utility", "b": "sharp or pointed", "c": "expensive", "d": "lawful"}, "ans": "a"},
        {"q": "Which sentence demonstrates the correct use of the past perfect continuous tense?", "opts": {"a": "The speaker had been practicing his presentation for hours before the electricity went out.", "b": "The speaker was practicing his presentation for hours before the electricity went out.", "c": "The speaker had practiced his presentation for hours before the electricity went out.", "d": "The speaker has been practicing his presentation since morning."}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'compliment' (praise)?", "opts": {"a": "complement (something that completes)", "b": "complaint", "c": "complicate", "d": "compliance"}, "ans": "a"},
        {"q": "In an oral presentation, if a speaker faces a hostile question from the audience during Q&A, they should:", "opts": {"a": "remain calm, listen carefully, and respond politely and objectively", "b": "argue heatedly with the questioner", "c": "ignore the questioner and walk off the stage", "d": "pretend not to hear the question"}, "ans": "a"},
        {"q": "What is the semantic purpose of a 'transition sentence' in a formal presentation?", "opts": {"a": "To bridge the flow between one main point and the next logically", "b": "To explain the biography of the author", "c": "To signal that the audience should ask questions", "d": "To translate English words to Somali"}, "ans": "a"},
        {"q": "Explain the metaphor 'poison at the bottom of the bowl' in Unit 1's poem.", "opts": {"a": "It suggests hidden malice, corruption, or treachery under a pleasant appearance", "b": "It refers to literal toxic substances in cooking", "c": "It represents ancient medicine practices", "d": "It describes the dirty water in a referral hospital"}, "ans": "a"},
        {"q": "Identify the word containing a prefix meaning 'again' or 'back' that is relevant to presentations.", "opts": {"a": "rehearse or review", "b": "deception", "c": "pointless", "d": "intonation"}, "ans": "a"},
        {"q": "Which of the following sentences contains a relative clause?", "opts": {"a": "The judges who are easily bought break the law.", "b": "The judges break the law because they are greedy.", "c": "The greedy judges break the law easily.", "d": "Breaking the law, the judges accepted bribes."}, "ans": "a"},
        {"q": "What is the past participle form of the verb 'shake'?", "opts": {"a": "shaken", "b": "shook", "c": "shaked", "d": "shaking"}, "ans": "a"},
        {"q": "A speaker changes their pitch and volume dynamically throughout a speech. This is called:", "opts": {"a": "vocal variety", "b": "monotone delivery", "c": "stuttered speech", "d": "syllable stress"}, "ans": "a"},
        {"q": "Which word is the most suitable synonym for 'disgrace'?", "opts": {"a": "shame or ignominy", "b": "honor", "c": "fame", "d": "pride"}, "ans": "a"},
        {"q": "Complete the conditional sentence: If the judge had not broken the law, he _____ arrested.", "opts": {"a": "would not have been", "b": "will not be", "c": "would not be", "d": "should not be"}, "ans": "a"},
        {"q": "Which of the following pairs contains true homophones?", "opts": {"a": "allowed / aloud", "b": "allow / alley", "c": "alloud / allied", "d": "alowed / allowed"}, "ans": "a"},
        {"q": "What punctuation mark is used to separate items in a list if the items themselves contain commas?", "opts": {"a": "Semicolon", "b": "Colon", "c": "Dash", "d": "Parentheses"}, "ans": "a"},
        {"q": "When a speaker uses rhetorical questions in a presentation, they aim to:", "opts": {"a": "engage the audience's thoughts without expecting an active answer", "b": "quiz the audience for a grade", "c": "hide the fact that they don't know the answer", "d": "shorten the presentation length"}, "ans": "a"},
        {"q": "What does the word 'outrage' mean in the poem's context?", "opts": {"a": "an extremely offensive or unjust act that arouses anger", "b": "a peaceful protest", "c": "a legal verdict", "d": "an expensive building"}, "ans": "a"},
        {"q": "Which sentence has correct subject-verb agreement?", "opts": {"a": "The list of presentation slides is ready.", "b": "The list of presentation slides are ready.", "c": "Each of the slides need to be edited.", "d": "Neither the slides nor the script are ready."}, "ans": "a"},
        {"q": "What is the grammatical term for the underlined phrase: 'Speaking in public' is an essential skill.", "opts": {"a": "Gerund phrase", "b": "Infinitive phrase", "c": "Prepositional phrase", "d": "Noun clause"}, "ans": "a"},
        {"q": "Which of these is a characteristic of a formal presentation slide design?", "opts": {"a": "High contrast text, consistent fonts, and simple layouts", "b": "Vibrant flashing colors and heavy animations", "c": "Paragraphs of text written in small font sizes", "d": "A different background image on each slide"}, "ans": "a"},
        {"q": "Identify the word with the correct spelling.", "opts": {"a": "questionnaire", "b": "questionaire", "c": "questionare", "d": "quesstionnaire"}, "ans": "a"},
        {"q": "What is the passive voice of: 'The audience will analyze the speech.'?", "opts": {"a": "The speech will be analyzed by the audience.", "b": "The speech would be analyzed by the audience.", "c": "The speech is analyzed by the audience.", "d": "The speech will analyze the audience."}, "ans": "a"},
        {"q": "In the sentence 'I wrote the love letter for YOU' (stress on you), what is the speaker's main target?", "opts": {"a": "Emphasizing the recipient, indicating it wasn't written for anyone else", "b": "Stressing that the letter was written in love", "c": "Proving that the writer did the work", "d": "Stressing that it was a letter and not a postcard"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'steel'?", "opts": {"a": "steal", "b": "still", "c": "stall", "d": "stale"}, "ans": "a"},
        {"q": "Which of these devices represents the repeating of a key word or phrase throughout a speech for emphasis?", "opts": {"a": "Repetition", "b": "Alliteration", "c": "Rhyme", "d": "Metaphor"}, "ans": "a"},
        {"q": "Identify the word containing a suffix that means 'full of' or 'characterized by'.", "opts": {"a": "painful", "b": "pointless", "c": "deception", "d": "forgetting"}, "ans": "a"},
        {"q": "What grammatical mood is used to express commands or direct requests, such as 'Never forget!'?", "opts": {"a": "Imperative mood", "b": "Indicative mood", "c": "Subjunctive mood", "d": "Interrogative mood"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch2_questions():
    # Chapter 2: Unit 3 & 4 (A Colossal House & Poetry Guide)
    # Focus: Description, Adjectives, Similes, Metaphors, Poetry, Rhythm, Stanza, Building Vocabulary.
    easy = [
        {"q": "What does the word 'colossal' mean?", "opts": {"a": "extremely large or huge", "b": "very tiny or small", "c": "colorful and bright", "d": "broken or ruined"}, "ans": "a"},
        {"q": "A comparison using 'like' or 'as' (e.g. 'as strong as an ox') is called a:", "opts": {"a": "simile", "b": "metaphor", "c": "personification", "d": "hyperbole"}, "ans": "a"},
        {"q": "Which word is an adjective describing a building?", "opts": {"a": "spacious", "b": "build", "c": "brick", "d": "slowly"}, "ans": "a"},
        {"q": "In poetry, a group of lines forming a unit is called a:", "opts": {"a": "stanza", "b": "paragraph", "c": "sentence", "d": "chapter"}, "ans": "a"},
        {"q": "A direct comparison that states one thing IS another (e.g. 'He is a lion in battle') is a:", "opts": {"a": "metaphor", "b": "simile", "c": "alliteration", "d": "personification"}, "ans": "a"},
        {"q": "What is the synonym of the word 'mansion'?", "opts": {"a": "large, grand house", "b": "small hut", "c": "apartment building", "d": "office tower"}, "ans": "a"},
        {"q": "Which of the following is a synonym of the word 'guide'?", "opts": {"a": "instructor or counselor", "b": "student", "c": "tourist", "d": "passenger"}, "ans": "a"},
        {"q": "Complete the simile: Her face was as white as _____.", "opts": {"a": "snow", "b": "coal", "c": "grass", "d": "brick"}, "ans": "a"},
        {"q": "Which of these is a sound device commonly found in poetry?", "opts": {"a": "Alliteration", "b": "Punctuation", "c": "Paragraphing", "d": "Capitalization"}, "ans": "a"},
        {"q": "What does a 'poetry guide' assist readers with?", "opts": {"a": "Understanding and analyzing poetic devices and structures", "b": "Writing shopping lists", "c": "Building brick walls", "d": "Calculating mathematics problems"}, "ans": "a"},
        {"q": "Which word describes a very old building that has fallen into decay?", "opts": {"a": "ruined or ancient", "b": "modern", "c": "renovated", "d": "spacious"}, "ans": "a"},
        {"q": "Complete the metaphor: Time is a _____.", "opts": {"a": "thief", "b": "like a thief", "c": "stealing things", "d": "passing quickly"}, "ans": "a"},
        {"q": "Which adjective describes a house with a lot of light?", "opts": {"a": "bright", "b": "dark", "c": "dusty", "d": "noisy"}, "ans": "a"},
        {"q": "What is the plural form of the word 'house'?", "opts": {"a": "houses", "b": "hice", "c": "housing", "d": "houseses"}, "ans": "a"},
        {"q": "Identify the adjective in the phrase: 'the colossal monument'.", "opts": {"a": "colossal", "b": "the", "c": "monument", "d": "is colossal"}, "ans": "a"},
        {"q": "Which word represents the rhythm of syllables in a line of poetry?", "opts": {"a": "Meter", "b": "Stanza", "c": "Theme", "d": "Alliteration"}, "ans": "a"},
        {"q": "Complete the phrase: A house made of _____ is very sturdy.", "opts": {"a": "bricks", "b": "paper", "c": "leaves", "d": "plastic"}, "ans": "a"},
        {"q": "What is the synonym of the word 'vast'?", "opts": {"a": "immense or huge", "b": "narrow", "c": "crowded", "d": "shallow"}, "ans": "a"},
        {"q": "In poetry, words that sound alike at the end of lines are said to:", "opts": {"a": "rhyme", "b": "alliterate", "c": "compare", "d": "statically sound"}, "ans": "a"},
        {"q": "Identify the noun in the sentence: 'The poetry books are on the shelf.'", "opts": {"a": "books", "b": "poetry (used as adjective)", "c": "on", "d": "are"}, "ans": "a"},
        {"q": "Which adjective describes a very comfortable and expensive house?", "opts": {"a": "luxurious", "b": "ruined", "c": "cramped", "d": "abandoned"}, "ans": "a"},
        {"q": "What is the base word of 'spaciousness'?", "opts": {"a": "space", "b": "spacious", "c": "spatial", "d": "spacing"}, "ans": "a"},
        {"q": "Which of these is a typical poetic theme?", "opts": {"a": "Love and mortality", "b": "Database configuration", "c": "Building construction contracts", "d": "Referral hospital layout"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "What is the main semantic difference between a 'simile' and a 'metaphor'?", "opts": {"a": "A simile compares using 'like' or 'as', whereas a metaphor compares by stating one thing is another directly", "b": "Similes are only used in prose, metaphors only in poems", "c": "Metaphors are longer than similes", "d": "Similes are harder to understand than metaphors"}, "ans": "a"},
        {"q": "Which of the following lines contains a clear metaphor?", "opts": {"a": "My home is my fortress.", "b": "My home is like a fortress.", "c": "My home is very secure.", "d": "My home has high walls."}, "ans": "a"},
        {"q": "What does a 'colossal house' suggest about the owner's status in ancient societies?", "opts": {"a": "High wealth, prestige, and power", "b": "Farming background and poverty", "c": "Religious isolation", "d": "Lack of architectural interest"}, "ans": "a"},
        {"q": "Which of the following is an adjective meaning 'magnificent and grand'?", "opts": {"a": "splendid", "b": "colossal", "c": "narrow", "d": "dilapidated"}, "ans": "a"},
        {"q": "In the line 'The wind whispered through the trees', which poetic device is used?", "opts": {"a": "Personification", "b": "Simile", "c": "Metaphor", "d": "Onomatopoeia"}, "ans": "a"},
        {"q": "Which word is a synonym for 'dilapidated' (describing a building)?", "opts": {"a": "run-down or in state of decay", "b": "brand new", "c": "costly", "d": "spacious"}, "ans": "a"},
        {"q": "In writing descriptive essays about buildings, which sensory details are most effective?", "opts": {"a": "Visual descriptions, textures, and sounds of the environment", "b": "A list of construction material costs", "c": "The builder's email address", "d": "A diagram of the plumbing system"}, "ans": "a"},
        {"q": "Complete: The new villa, _____ was built last year, stands on top of the hill.", "opts": {"a": "which", "b": "who", "c": "whom", "d": "whose"}, "ans": "a"},
        {"q": "What is the antonym of the word 'spacious'?", "opts": {"a": "cramped or confined", "b": "vast", "c": "huge", "d": "luxurious"}, "ans": "a"},
        {"q": "Which of these lines is an example of alliteration?", "opts": {"a": "Peter Piper picked a peck of pickled peppers.", "b": "He was as strong as a bull.", "c": "The ocean was a dark blue sheet.", "d": "Clang went the hammer on the brick."}, "ans": "a"},
        {"q": "What does the word 'rhythm' in poetry refer to?", "opts": {"a": "The regular pattern of stressed and unstressed syllables", "b": "The total number of lines in a stanza", "c": "The vocabulary definition list", "d": "The font used to print the poem"}, "ans": "a"},
        {"q": "Which suffix can be added to the noun 'beauty' to make it an adjective?", "opts": {"a": "-ful (beautiful)", "b": "-less", "c": "-ize", "d": "-ly"}, "ans": "a"},
        {"q": "Identify the relative pronoun in: 'The house whose roof was damaged has been repaired.'", "opts": {"a": "whose", "b": "roof", "c": "damaged", "d": "has been"}, "ans": "a"},
        {"q": "Which word refers to a room right under the roof of a house, often used for storage?", "opts": {"a": "attic", "b": "basement", "c": "lounge", "d": "corridor"}, "ans": "a"},
        {"q": "What is 'imagery' in literature?", "opts": {"a": "The use of descriptive language that appeals to the physical senses", "b": "Printing photos in the textbook", "c": "Creating a list of chapters", "d": "Analyzing the font size of headings"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'hall'?", "opts": {"a": "haul", "b": "hill", "c": "hole", "d": "hell"}, "ans": "a"},
        {"q": "Complete: The colossal mansion, which had been abandoned for decades, _____ a spooky look.", "opts": {"a": "had", "b": "has", "c": "is having", "d": "will have"}, "ans": "a"},
        {"q": "Which descriptive adjective fits a dark and wet basement?", "opts": {"a": "dank", "b": "bright", "c": "dry", "d": "airy"}, "ans": "a"},
        {"q": "What is the term for the repetition of similar vowel sounds inside words in a line of poetry?", "opts": {"a": "Assonance", "b": "Alliteration", "c": "Consonance", "d": "Rhyme"}, "ans": "a"},
        {"q": "Which sentence contains a non-defining relative clause?", "opts": {"a": "The castle, which was built in the 14th century, is now a tourist attraction.", "b": "The castle which was built in the 14th century is now a tourist attraction.", "c": "The castle was built in the 14th century and it is a tourist attraction.", "d": "Building the castle in the 14th century made it a tourist attraction."}, "ans": "a"},
        {"q": "Which word is a synonym for 'dwelling'?", "opts": {"a": "residence or home", "b": "office", "c": "school", "d": "hospital"}, "ans": "a"},
        {"q": "Identify the word containing a prefix meaning 'under' that describes a level of a house.", "opts": {"a": "substructure", "b": "superstructure", "c": "architecture", "d": "infrastructure"}, "ans": "a"},
        {"q": "Complete: The poet uses a metaphor to describe the moon as a 'silver _____ in the dark sky'.", "opts": {"a": "coin", "b": "like a coin", "c": "shining", "d": "brightly"}, "ans": "a"},
        {"q": "Which adjective describes a house that is warm, comfortable, and inviting?", "opts": {"a": "cozy", "b": "vast", "c": "damp", "d": "dilapidated"}, "ans": "a"},
        {"q": "What is the past tense of the verb 'build'?", "opts": {"a": "built", "b": "builded", "c": "building", "d": "builds"}, "ans": "a"},
        {"q": "In a poetry guide, the literal dictionary definition of a word is called its _____ meaning.", "opts": {"a": "denotative", "b": "connotative", "c": "metaphorical", "d": "figurative"}, "ans": "a"},
        {"q": "Which word is a homophone of the word 'ceiling'?", "opts": {"a": "sealing", "b": "sailing", "c": "selling", "d": "soiling"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Which of the following describes the literary term 'connotation'?", "opts": {"a": "The cultural or emotional association that a word carries beyond its literal definition", "b": "The literal, dictionary definition of a word", "c": "The rhyme pattern of a poem's lines", "d": "The process of doubling consonants in past tense"}, "ans": "a"},
        {"q": "In describing architectural layouts, what is the semantic difference between a 'corridor' and a 'vestibule'?", "opts": {"a": "A corridor is a long passage linking rooms, while a vestibule is an entrance hall or lobby", "b": "A vestibule is located on the roof, a corridor in the basement", "c": "A corridor is luxurious, a vestibule is dilapidated", "d": "There is no difference; they are exact synonyms"}, "ans": "a"},
        {"q": "Identify the figure of speech in: 'The colossal castle stood as a silent sentinel guarding the valley.'", "opts": {"a": "Personification and Metaphor", "b": "Simile and Onomatopoeia", "c": "Alliteration and Hyperbole", "d": "No figure of speech is present"}, "ans": "a"},
        {"q": "Which sentence contains a correctly formatted defining relative clause?", "opts": {"a": "The materials that were used to build the colossal house were imported.", "b": "The materials, that were used to build the colossal house, were imported.", "c": "The materials, which were used to build the colossal house, were imported.", "d": "The materials used to build the colossal house, which were imported."}, "ans": "a"},
        {"q": "In the analysis of poetic structure, what does 'enjambment' refer to?", "opts": {"a": "The running over of a sentence or phrase from one poetic line to the next without terminal punctuation", "b": "The pattern of repeating initial consonant sounds", "c": "The emotional tone of the poem's conclusion", "d": "A stanza of exactly four lines"}, "ans": "a"},
        {"q": "What is the term for a stanza consisting of exactly four lines, often with alternating rhymes?", "opts": {"a": "Quatrain", "b": "Couplet", "c": "Sestet", "d": "Octave"}, "ans": "a"},
        {"q": "Which word is spelled correctly to describe a spacious, columned porch surrounding a house?", "opts": {"a": "veranda", "b": "varandah", "c": "verandah", "d": "viranda"}, "ans": "a"},
        {"q": "Identify the grammatical structure of the phrase 'having been built of stone' in: 'The house, having been built of stone, withstood the storm.'", "opts": {"a": "Participle phrase acting as adjective", "b": "Gerund phrase acting as subject", "c": "Relative clause", "d": "Prepositional phrase"}, "ans": "a"},
        {"q": "Which adjective describes a style of architecture characterized by pointed arches, ribbed vaults, and flying buttresses?", "opts": {"a": "Gothic", "b": "Baroque", "c": "Modernist", "d": "Classical"}, "ans": "a"},
        {"q": "In the phrase 'the house is a sanctuary', the word 'sanctuary' connotes:", "opts": {"a": "safety, peace, and protection", "b": "imprisonment and isolation", "c": "monetary value and luxury", "d": "construction labor and noise"}, "ans": "a"},
        {"q": "Which word is a synonym for 'immense' that is relevant to colossal structures?", "opts": {"a": "gargantuan or monumental", "b": "microscopic", "c": "transient", "d": "narrow"}, "ans": "a"},
        {"q": "Complete the sentence: If they had hired a skilled architect, the colossal house _____ built much faster.", "opts": {"a": "would have been", "b": "will be", "c": "would be", "d": "should have"}, "ans": "a"},
        {"q": "What is the phonetic spelling of the word 'architecture'?", "opts": {"a": "/ˈɑːrkɪtektʃər/", "b": "/ɑːrtʃɪtektʃər/", "c": "/ˈɑːrkɪtekt/", "d": "/ɑːrkɪtektʃuːr/"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'site' (location)?", "opts": {"a": "sight (vision) or cite (quote)", "b": "seat", "c": "suit", "d": "sot"}, "ans": "a"},
        {"q": "In a poem, the attitude of the author towards the subject matter is referred to as the:", "opts": {"a": "tone", "b": "theme", "c": "meter", "d": "rhyme"}, "ans": "a"},
        {"q": "Which word is the antonym of 'colossal'?", "opts": {"a": "minuscule or tiny", "b": "mammoth", "c": "vast", "d": "spacious"}, "ans": "a"},
        {"q": "What is the plural of 'oasis'?", "opts": {"a": "oases", "b": "oasises", "c": "oasis", "d": "oasise"}, "ans": "a"},
        {"q": "In the sentence: 'The architect who designed the building won an award', what type of clause is 'who designed the building'?", "opts": {"a": "Defining relative clause", "b": "Non-defining relative clause", "c": "Adverbial clause", "d": "Noun clause"}, "ans": "a"},
        {"q": "Which of these is a key aspect of 'descriptive writing style'?", "opts": {"a": "Using vivid adjectives, active verbs, and figures of speech to paint a picture in the reader's mind", "b": "Presenting statistical charts and lists of facts chronologically", "c": "Listing instructions line-by-line", "d": "Writing dialogues without tag words"}, "ans": "a"},
        {"q": "What does a 'couplet' refer to in poetry?", "opts": {"a": "Two consecutive lines of verse, usually in the same meter and joined by rhyme", "b": "A stanza of four lines", "c": "A poem containing exactly eighteen lines", "d": "The comparison of a house to a castle"}, "ans": "a"},
        {"q": "Which prefix can be added to the word 'structure' to mean the secondary structure built on top of a foundation?", "opts": {"a": "super- (superstructure)", "b": "infra-", "c": "sub-", "d": "de-"}, "ans": "a"},
        {"q": "Complete: The spacious courtyard, the walls of which _____ decorated with murals, welcomed the guests.", "opts": {"a": "were", "b": "was", "c": "is", "d": "are"}, "ans": "a"},
        {"q": "What is the synonym of the word 'abode'?", "opts": {"a": "dwelling place or home", "b": "office room", "c": "commercial street", "d": "construction tool"}, "ans": "a"},
        {"q": "Identify the poetic device: 'The teapot sang a merry tune on the stove.'", "opts": {"a": "Personification", "b": "Simile", "c": "Metaphor", "d": "Alliteration"}, "ans": "a"},
        {"q": "Which sentence shows the correct use of double adjectives before a noun describing a house?", "opts": {"a": "They bought a beautiful, colossal stone house.", "b": "They bought a stone colossal beautiful house.", "c": "They bought a colossal stone beautiful house.", "d": "They bought a beautiful stone colossal house."}, "ans": "a"},
        {"q": "In the analysis of meter, a foot containing a stressed syllable followed by an unstressed syllable is a:", "opts": {"a": "trochee", "b": "iamb", "c": "anapest", "d": "dactyl"}, "ans": "a"},
        {"q": "Which word is a homophone for the word 'aisle' (passage between rows)?", "opts": {"a": "isle (island) or I'll (I will)", "b": "ail", "c": "ale", "d": "all"}, "ans": "a"},
        {"q": "What is the primary role of 'sensory language' in descriptive writing?", "opts": {"a": "To engage the reader's senses of sight, sound, touch, smell, and taste", "b": "To simplify the grammar of the essay", "c": "To write formal summaries", "d": "To analyze the rhyme scheme of a poem"}, "ans": "a"},
        {"q": "Identify the prefix in the word 'infrastructure'.", "opts": {"a": "infra- (meaning below or underneath)", "b": "infra- (meaning above)", "c": "in-", "d": "infra- (meaning green)"}, "ans": "a"},
        {"q": "What is the term for a line of poetry consisting of five iambic feet?", "opts": {"a": "Iambic pentameter", "b": "Iambic tetrameter", "c": "Trochaic pentameter", "d": "Free verse"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch3_questions():
    # Chapter 3: Unit 5 & 6 (The Lion with a Thorn in His Paw & Oral Literature)
    # Focus: Fables, Tales, Moral Lessons, Simple Past Tense, Conjunctions, Proverbs, Oral Literature.
    easy = [
        {"q": "What is a 'fable'?", "opts": {"a": "A short story, typically with animals as characters, conveying a moral lesson", "b": "A detailed history textbook of a nation", "c": "A modern scientific report on lions", "d": "A travel questionnaire design"}, "ans": "a"},
        {"q": "What did the lion have in his paw in the Unit 5 story?", "opts": {"a": "A sharp thorn", "b": "A gold coin", "c": "A piece of glass", "d": "A plastic bag"}, "ans": "a"},
        {"q": "Which of the following is a simple past tense verb?", "opts": {"a": "helped", "b": "help", "c": "helping", "d": "helps"}, "ans": "a"},
        {"q": "What is the moral of a story?", "opts": {"a": "The lesson that the story teaches about right and wrong behavior", "b": "The names of the main characters", "c": "The page number where the story ends", "d": "The price of the storybook"}, "ans": "a"},
        {"q": "Which word is a coordinating conjunction?", "opts": {"a": "but", "b": "because", "c": "although", "d": "since"}, "ans": "a"},
        {"q": "A traditional story passed down through generations by word of mouth is called:", "opts": {"a": "oral literature or folktale", "b": "written essay", "c": "newspaper report", "d": "email chain"}, "ans": "a"},
        {"q": "What is the past tense of the verb 'run'?", "opts": {"a": "ran", "b": "runned", "c": "running", "d": "runs"}, "ans": "a"},
        {"q": "Complete the proverb: Actions speak louder than _____.", "opts": {"a": "words", "b": "speeches", "c": "voices", "d": "poems"}, "ans": "a"},
        {"q": "Which animal is traditionally portrayed as clever or tricky in Somali folktales?", "opts": {"a": "The jackal", "b": "The lion", "c": "The camel", "d": "The sheep"}, "ans": "a"},
        {"q": "Which of the following is a subordinating conjunction?", "opts": {"a": "because", "b": "and", "c": "or", "d": "so"}, "ans": "a"},
        {"q": "What did the shepherd do when he found the lion with a thorn in its paw?", "opts": {"a": "He pulled the thorn out to relieve the lion's pain", "b": "He ran away screaming", "c": "He threw stones at the lion", "d": "He built a colossal house around the lion"}, "ans": "a"},
        {"q": "What is the past tense of the verb 'see'?", "opts": {"a": "saw", "b": "seen", "c": "seed", "d": "sees"}, "ans": "a"},
        {"q": "Complete: The lion roared loudly _____ it was in severe pain.", "opts": {"a": "because", "b": "but", "c": "although", "d": "or"}, "ans": "a"},
        {"q": "Which of the following is an example of oral literature?", "opts": {"a": "Riddles and proverbs told by grandparents", "b": "A printed instruction guide for database backup", "c": "A text message sent to a friend", "d": "A database schema table"}, "ans": "a"},
        {"q": "What is the past tense of the verb 'tell'?", "opts": {"a": "told", "b": "telled", "c": "telling", "d": "tells"}, "ans": "a"},
        {"q": "Identify the conjunction: 'We wanted to go out, but it started to rain.'", "opts": {"a": "but", "b": "wanted", "c": "to", "d": "started"}, "ans": "a"},
        {"q": "In the story, the lion showed _____ to the man who helped him.", "opts": {"a": "gratitude", "b": "anger", "c": "fear", "d": "deception"}, "ans": "a"},
        {"q": "What is the past tense of the verb 'go'?", "opts": {"a": "went", "b": "gone", "c": "goes", "d": "going"}, "ans": "a"},
        {"q": "Complete: A proverb is a short, well-known saying that expresses a truth or _____.", "opts": {"a": "piece of advice", "b": "mathematical formula", "c": "spelling mistake", "d": "relative clause"}, "ans": "a"},
        {"q": "Identify the past tense verb: 'The bird flew away.'", "opts": {"a": "flew", "b": "bird", "c": "away", "d": "fly"}, "ans": "a"},
        {"q": "Which conjunction shows a contrast between two ideas?", "opts": {"a": "although", "b": "and", "c": "so", "d": "because"}, "ans": "a"},
        {"q": "What is the past tense of the verb 'pull'?", "opts": {"a": "pulled", "b": "pulling", "c": "pulls", "d": "pull"}, "ans": "a"},
        {"q": "Oral literature is preserved primarily through:", "opts": {"a": "speech and memorization", "b": "printing houses", "c": "hard disks", "d": "written manuscripts"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "In fables, why are animal characters typically used instead of humans?", "opts": {"a": "To present human weaknesses and lessons in a simplified, non-offensive, and universal way", "b": "Because animals are easier to write about", "c": "To teach children about biology and zoology", "d": "Because ancient people did not have human names"}, "ans": "a"},
        {"q": "Which conjunction is best suited to combine these sentences: 'The shepherd was terrified. He decided to help the roaring lion.'?", "opts": {"a": "Although the shepherd was terrified, he decided to help the roaring lion.", "b": "The shepherd was terrified because he decided to help the roaring lion.", "c": "The shepherd was terrified so he decided to help the roaring lion.", "d": "The shepherd was terrified or he decided to help the roaring lion."}, "ans": "a"},
        {"q": "What is the meaning of the Somali proverb 'A key to the grave is better than a key to a bad home'?", "opts": {"a": "It highlights the supreme value of peace and dignity over a toxic living environment", "b": "It lists the pricing of grave materials", "c": "It gives instructions on lock picking", "d": "It discusses the architecture of houses"}, "ans": "a"},
        {"q": "What is the main function of 'subordinating conjunctions'?", "opts": {"a": "To join an independent clause to a dependent clause, showing a relationship of cause, time, or condition", "b": "To list nouns in alphabetical order", "c": "To end a sentence with finality", "d": "To introduce a direct quote"}, "ans": "a"},
        {"q": "Which sentence uses the simple past tense correctly for an irregular verb?", "opts": {"a": "The lion slept peacefully after the thorn was removed.", "b": "The lion sleeped peacefully after the thorn was removed.", "c": "The lion was sleep peacefully after the thorn was removed.", "d": "The lion has slept peacefully after the thorn was removed."}, "ans": "a"},
        {"q": "What are the common genres of oral literature?", "opts": {"a": "Folktales, riddles, myths, legends, proverbs, and poetry", "b": "Newspaper columns and scientific articles", "c": "Database manuals and coding documentation", "d": "E-books and email chains"}, "ans": "a"},
        {"q": "Complete: The shepherd did not run away, _____ did he show any signs of aggression.", "opts": {"a": "nor", "b": "or", "c": "but", "d": "so"}, "ans": "a"},
        {"q": "Identify the subordinate clause in: 'When the lion roared, the shepherd stopped walking.'", "opts": {"a": "When the lion roared", "b": "the shepherd stopped walking", "c": "the shepherd stopped", "d": "roared, the shepherd"}, "ans": "a"},
        {"q": "What does the word 'gratitude' mean in the fable?", "opts": {"a": "thankfulness and appreciation for a kindness received", "b": "greed and selfishness", "c": "fear and cowardice", "d": "deception and trickery"}, "ans": "a"},
        {"q": "Which of the following sentences contains a past continuous verb?", "opts": {"a": "The lion was crying in pain when the shepherd found him.", "b": "The lion cried in pain when the shepherd found him.", "c": "The lion has cried in pain when the shepherd found him.", "d": "The lion cries in pain when the shepherd finds him."}, "ans": "a"},
        {"q": "What grammatical error is present in: 'The shepherd pulled the thorn out and then the lion runned into the forest.'?", "opts": {"a": "Incorrect past tense form of the verb 'run' ('runned' instead of 'ran')", "b": "Use of coordinating conjunction 'and'", "c": "Spelling of 'thorn'", "d": "Punctuation mark at the end"}, "ans": "a"},
        {"q": "Which conjunction expresses a condition?", "opts": {"a": "unless or if", "b": "although", "c": "because", "d": "and"}, "ans": "a"},
        {"q": "What is the past tense of the irregular verb 'bite'?", "opts": {"a": "bit", "b": "bited", "c": "bitten", "d": "biting"}, "ans": "a"},
        {"q": "In oral traditions, a story that explains the origin of a natural phenomenon is called a:", "opts": {"a": "myth", "b": "fable", "c": "riddle", "d": "novel"}, "ans": "a"},
        {"q": "Complete: The lion did not attack the shepherd; _____, it licked his hand gently.", "opts": {"a": "instead", "b": "therefore", "c": "consequently", "d": "otherwise"}, "ans": "a"},
        {"q": "Identify the conjunction in: 'You can have either the apple or the banana.'", "opts": {"a": "either...or", "b": "can", "c": "have", "d": "apple"}, "ans": "a"},
        {"q": "What is the past tense of the irregular verb 'catch'?", "opts": {"a": "caught", "b": "catched", "c": "catching", "d": "catches"}, "ans": "a"},
        {"q": "In the sentence 'She walked home because it was dark', what is the function of 'because'?", "opts": {"a": "It introduces a clause giving a reason", "b": "It shows a contrast of ideas", "c": "It indicates a time sequence", "d": "It introduces a conditional state"}, "ans": "a"},
        {"q": "Which of these is a typical function of proverbs in African societies?", "opts": {"a": "To advise, educate, resolve conflicts, and pass down societal values concisely", "b": "To replace written dictionaries", "c": "To construct poetry rhyme schemes", "d": "To serve as legal evidence in court"}, "ans": "a"},
        {"q": "Complete: While the shepherd _____ the lion's paw, the beast stayed completely still.", "opts": {"a": "was examining", "b": "examined", "c": "had examined", "d": "examines"}, "ans": "a"},
        {"q": "What is the past tense of 'strike'?", "opts": {"a": "struck", "b": "striked", "c": "stricken", "d": "strikes"}, "ans": "a"},
        {"q": "Identify the correlative conjunction in the sentence: 'Neither the lion nor the shepherd moved.'", "opts": {"a": "Neither...nor", "b": "lion", "c": "shepherd", "d": "moved"}, "ans": "a"},
        {"q": "What is the antonym of the word 'tame'?", "opts": {"a": "wild or savage", "b": "gentle", "c": "obedient", "d": "trained"}, "ans": "a"},
        {"q": "Complete: The man did not have weapons, _____ did he feel any desire to fight.", "opts": {"a": "nor", "b": "or", "c": "but", "d": "so"}, "ans": "a"},
        {"q": "What is the past tense of 'hide'?", "opts": {"a": "hid", "b": "hided", "c": "hidden", "d": "hides"}, "ans": "a"},
        {"q": "In literature, the main character who faces conflict in a narrative is called the:", "opts": {"a": "protagonist", "b": "antagonist", "c": "narrator", "d": "villain"}, "ans": "a"},
        {"q": "Which conjunction is used to show result?", "opts": {"a": "so or therefore", "b": "although", "c": "but", "d": "because"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Which of the following sentences correctly utilizes a subordinating conjunction of concession?", "opts": {"a": "Although the lion was immensely powerful, it submitted quietly to the shepherd's touch.", "b": "The lion was immensely powerful, but it submitted quietly to the shepherd's touch.", "c": "The lion was immensely powerful, so it submitted quietly to the shepherd's touch.", "d": "The lion was immensely powerful because it submitted quietly to the shepherd's touch."}, "ans": "a"},
        {"q": "In oral literature, how do 'folktales' differ structurally and semantically from 'legends'?", "opts": {"a": "Folktales are fictional narratives conveying moral truths, whereas legends are historically-grounded stories about heroic figures", "b": "Folktales are written, legends are purely oral", "c": "Legends always have animal characters, folktales do not", "d": "There is no difference; they are exact synonyms"}, "ans": "a"},
        {"q": "Analyze the syntax: 'Scarcely had the shepherd pulled the thorn out when the lion bounded away.' What does this structure emphasize?", "opts": {"a": "The immediacy of the lion's departure after the action of pulling", "b": "The difficulty of pulling the thorn out", "c": "The shepherd's fear during the operation", "d": "The lion's anger towards the shepherd"}, "ans": "a"},
        {"q": "What is the past tense of the irregular verb 'slink'?", "opts": {"a": "slunk", "b": "slinked", "c": "slank", "d": "slinking"}, "ans": "a"},
        {"q": "In narrative structure, what is the 'exposition' phase?", "opts": {"a": "The introductory section that establishes characters, setting, and basic situation", "b": "The climax where the conflict is resolved", "c": "The list of vocabulary words at the end", "d": "The publisher information page"}, "ans": "a"},
        {"q": "Which of the following is a subordinating conjunction of time?", "opts": {"a": "as soon as", "b": "although", "c": "provided that", "d": "so that"}, "ans": "a"},
        {"q": "What does the word 'beast' connote in classical fables?", "opts": {"a": "raw power, wild nature, and lack of human rationality", "b": "kindness and domestication", "c": "weakness and disease", "d": "high wealth and status"}, "ans": "a"},
        {"q": "Complete the sentence using the past perfect subjunctive: If the shepherd _____ the lion, the beast would have died of infection.", "opts": {"a": "had not helped", "b": "did not help", "c": "would not help", "d": "has not helped"}, "ans": "a"},
        {"q": "Identify the correlative conjunction in: 'Whether you like it or not, you must tell the folktale.'", "opts": {"a": "Whether...or", "b": "like", "c": "must", "d": "folktale"}, "ans": "a"},
        {"q": "What is the past tense of the irregular verb 'bleed'?", "opts": {"a": "bled", "b": "bleeded", "c": "bleeding", "d": "bleeds"}, "ans": "a"},
        {"q": "In oral storytelling, which of the following techniques is most critical for holding the audience's attention?", "opts": {"a": "Varying pitch/tone, using gestures, and involving the audience directly", "b": "Reading verbatim from a printed paper script", "c": "Standing completely still with no expressions", "d": "Speaking as fast as possible in a whisper"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'tale' (story)?", "opts": {"a": "tail (animal part) or tale (spelled similarly but contextually different)", "b": "tall", "c": "teal", "d": "toll"}, "ans": "a"},
        {"q": "What is the past tense of 'bind'?", "opts": {"a": "bound", "b": "binded", "c": "bounden", "d": "binds"}, "ans": "a"},
        {"q": "Which sentence contains a correctly punctuated adverbial clause at the beginning?", "opts": {"a": "While the lion was sleeping, the shepherd searched for a way to escape.", "b": "While the lion was sleeping the shepherd searched for a way to escape.", "c": "While the lion was sleeping, the shepherd, searched for a way to escape.", "d": "While, the lion was sleeping, the shepherd searched for a way to escape."}, "ans": "a"},
        {"q": "What is the term for a story within a story, often used in traditional oral frameworks?", "opts": {"a": "Frame narrative", "b": "Monologue", "c": "Alliteration", "d": "Stanza"}, "ans": "a"},
        {"q": "Which word is a synonym for 'moral'?", "opts": {"a": "ethical lesson or principle", "b": "story length", "c": "narrator name", "d": "character trait"}, "ans": "a"},
        {"q": "What is the past tense of the irregular verb 'deal'?", "opts": {"a": "dealt", "b": "dealed", "c": "dealing", "d": "deals"}, "ans": "a"},
        {"q": "In the sentence: 'The shepherd acted quickly lest the lion should bite him', what does 'lest' mean?", "opts": {"a": "to prevent the possibility that; for fear that", "b": "because", "c": "although", "d": "so that"}, "ans": "a"},
        {"q": "Which of the following is a features of oral literature?", "opts": {"a": "It is dynamic, performance-based, and relies on memory and oral transmission", "b": "It is static, fixed in print, and has a single verified author", "c": "It is written in high-level computer code", "d": "It lacks any structure or genres"}, "ans": "a"},
        {"q": "Complete the proverb: A bird in the hand is worth _____ in the bush.", "opts": {"a": "two", "b": "three", "c": "one", "d": "none"}, "ans": "a"},
        {"q": "What is the past tense of 'cling'?", "opts": {"a": "clung", "b": "clinged", "c": "clang", "d": "clings"}, "ans": "a"},
        {"q": "Identify the conjunction that shows a condition in: 'I will go provided that you accompany me.'", "opts": {"a": "provided that", "b": "will", "c": "go", "d": "accompany"}, "ans": "a"},
        {"q": "What is the synonym of the word 'lore' in folklore?", "opts": {"a": "traditional knowledge or beliefs", "b": "spelling rules", "c": "page layout", "d": "storyteller"}, "ans": "a"},
        {"q": "Complete: No sooner had the shepherd pulled the thorn out _____ the lion let out a roar of relief.", "opts": {"a": "than", "b": "then", "c": "when", "d": "before"}, "ans": "a"},
        {"q": "What is the past tense of 'grind'?", "opts": {"a": "ground", "b": "grinded", "c": "granded", "d": "grinds"}, "ans": "a"},
        {"q": "In literary analysis, the perspective from which a story is told is called the:", "opts": {"a": "point of view", "b": "theme", "c": "climax", "d": "conflict"}, "ans": "a"},
        {"q": "Which conjunction is used to express a negative condition?", "opts": {"a": "unless", "b": "if", "c": "whether", "d": "provided"}, "ans": "a"},
        {"q": "What is the past tense of 'shrink'?", "opts": {"a": "shrank", "b": "shrinked", "c": "shrunk", "d": "shrinks"}, "ans": "a"},
        {"q": "Identify the word containing a suffix meaning 'state or condition of' that is relevant to narratives.", "opts": {"a": "brotherhood or falsehood", "b": "helped", "c": "cleverly", "d": "conjunction"}, "ans": "a"},
        {"q": "What grammatical structure is used in: 'Had he known the lion was friendly, he wouldn't have run.'?", "opts": {"a": "Inverted third conditional", "b": "First conditional", "c": "Past continuous", "d": "Relative clause"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch4_questions():
    # Chapter 4: Unit 7 & 8 (The Father and his Son & Edible Soda)
    # Focus: Family Vocabulary, Chemistry/Cooking Vocabulary, Soda/Compounds, States of Matter, Direct vs Indirect Speech, Modals.
    easy = [
        {"q": "What is the term for a substance formed by the chemical combination of two or more elements?", "opts": {"a": "Compound", "b": "Element", "c": "Mixture", "d": "Gas"}, "ans": "a"},
        {"q": "Which of these is a state of matter?", "opts": {"a": "Solid", "b": "Atom", "c": "Acid", "d": "Molecule"}, "ans": "a"},
        {"q": "What is 'edible soda' commonly used for in households?", "opts": {"a": "Baking and cleaning", "b": "Fueling cars", "c": "Writing books", "d": "Database storage"}, "ans": "a"},
        {"q": "In English grammar, when we report someone's words exactly, we use:", "opts": {"a": "Direct speech", "b": "Indirect speech", "c": "Passive voice", "d": "Relative clauses"}, "ans": "a"},
        {"q": "Which word describes the relationship of a male child to his father?", "opts": {"a": "son", "b": "daughter", "c": "brother", "d": "cousin"}, "ans": "a"},
        {"q": "What is the chemical formula of water?", "opts": {"a": "H2O", "b": "CO2", "c": "NaCl", "d": "O2"}, "ans": "a"},
        {"q": "Which of these verbs is a modal verb?", "opts": {"a": "must", "b": "clean", "c": "father", "d": "dissolve"}, "ans": "a"},
        {"q": "Complete the direct speech: He said, 'I _____ tired.'", "opts": {"a": "am", "b": "was", "c": "been", "d": "is"}, "ans": "a"},
        {"q": "What state of matter is steam?", "opts": {"a": "Gas", "b": "Solid", "c": "Liquid", "d": "Compound"}, "ans": "a"},
        {"q": "What is the synonym of the word 'edible'?", "opts": {"a": "safe to eat", "b": "poisonous", "c": "hard", "d": "expensive"}, "ans": "a"},
        {"q": "In the story 'The Father and his Son', what is the main lesson?", "opts": {"a": "The importance of respecting parental guidance and family wisdom", "b": "How to mix chemical compounds", "c": "The speed of direct deployment", "d": "How to write coding structures"}, "ans": "a"},
        {"q": "Which of these is a liquid at room temperature?", "opts": {"a": "Water", "b": "Ice", "c": "Steam", "d": "Oxygen"}, "ans": "a"},
        {"q": "Complete: The father told his son that he _____ proud of him.", "opts": {"a": "was", "b": "is", "c": "am", "d": "be"}, "ans": "a"},
        {"q": "What gas do we breathe out that is also in soda drinks?", "opts": {"a": "Carbon dioxide", "b": "Oxygen", "c": "Nitrogen", "d": "Hydrogen"}, "ans": "a"},
        {"q": "Which modal verb shows ability?", "opts": {"a": "can", "b": "must", "c": "should", "d": "might"}, "ans": "a"},
        {"q": "What is the past tense of 'say'?", "opts": {"a": "said", "b": "sayed", "c": "saying", "d": "says"}, "ans": "a"},
        {"q": "Complete: Water freezes to become a _____, which is ice.", "opts": {"a": "solid", "b": "liquid", "c": "gas", "d": "compound"}, "ans": "a"},
        {"q": "What is the synonym of 'parent'?", "opts": {"a": "father or mother", "b": "son", "c": "brother", "d": "uncle"}, "ans": "a"},
        {"q": "Identify the modal verb in: 'You should listen to your father.'", "opts": {"a": "should", "b": "listen", "c": "to", "d": "father"}, "ans": "a"},
        {"q": "What happens when you mix baking soda with an acid like vinegar?", "opts": {"a": "It reacts and produces gas bubbles", "b": "It freezes immediately", "c": "It turns into solid gold", "d": "Nothing happens"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'son'?", "opts": {"a": "sun", "b": "sin", "c": "sown", "d": "soon"}, "ans": "a"},
        {"q": "Identify the reporting verb in: 'The boy asked his father for help.'", "opts": {"a": "asked", "b": "boy", "c": "father", "d": "help"}, "ans": "a"},
        {"q": "What is the chemical name of common table salt?", "opts": {"a": "Sodium chloride", "b": "Sodium bicarbonate", "c": "Carbon dioxide", "d": "Calcium carbonate"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "When converting direct speech to indirect speech, if the reporting verb is in the past tense, what happens to the present simple tense in the reported clause?", "opts": {"a": "It shifts back to the simple past tense", "b": "It remains in the present simple tense", "c": "It changes to the future tense", "d": "It becomes a relative clause"}, "ans": "a"},
        {"q": "Which of the following represents the correct indirect speech for: 'The father said, \"I am mixing the soda solution now.\"'?", "opts": {"a": "The father said that he was mixing the soda solution then.", "b": "The father said that I am mixing the soda solution now.", "c": "The father said that he is mixing the soda solution now.", "d": "The father said he mixed the soda solution now."}, "ans": "a"},
        {"q": "What chemical compound is baking soda?", "opts": {"a": "Sodium bicarbonate (NaHCO3)", "b": "Sodium chloride (NaCl)", "c": "Carbon dioxide (CO2)", "d": "Calcium carbonate (CaCO3)"}, "ans": "a"},
        {"q": "How do 'atoms' relate to 'molecules' structurally?", "opts": {"a": "Atoms are the basic units of matter, which combine to form molecules", "b": "Molecules are smaller than atoms", "c": "Atoms are mixtures, molecules are elements", "d": "There is no relation between them"}, "ans": "a"},
        {"q": "Which modal verb is most appropriate to express a polite request?", "opts": {"a": "Could you please pass the baking soda?", "b": "Must you pass the baking soda?", "c": "Should you pass the baking soda?", "d": "Shall you pass the baking soda?"}, "ans": "a"},
        {"q": "What is the meaning of the word 'dissolve' in chemistry?", "opts": {"a": "To incorporate a solid ingredient into a liquid so that it becomes a solution", "b": "To freeze a liquid into a solid state", "c": "To split a molecule into atoms by heating", "d": "To release carbon dioxide gas"}, "ans": "a"},
        {"q": "Which sentence uses the correct reporting verb for a question?", "opts": {"a": "The father inquired whether the solution had dissolved.", "b": "The father said whether the solution had dissolved.", "c": "The father told whether the solution had dissolved.", "d": "The father reported whether the solution had dissolved."}, "ans": "a"},
        {"q": "Identify the state of matter of the substance in: 'A substance that has a definite volume but takes the shape of its container.'", "opts": {"a": "Liquid", "b": "Solid", "c": "Gas", "d": "Plasma"}, "ans": "a"},
        {"q": "What is the synonym of the word 'nurture' in the context of family?", "opts": {"a": "care for and encourage the growth of", "b": "neglect", "c": "punish", "d": "deceive"}, "ans": "a"},
        {"q": "Complete the sentence: In a chemical laboratory, you _____ wear safety goggles at all times.", "opts": {"a": "must", "b": "might", "c": "could", "d": "would"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'meat'?", "opts": {"a": "meet (encounter) or mete (distribute)", "b": "mate", "c": "mitt", "d": "met"}, "ans": "a"},
        {"q": "How does 'indirect speech' handle indicators of time like 'tomorrow'?", "opts": {"a": "It shifts them to terms like 'the next day' or 'the following day'", "b": "It keeps them exactly as 'tomorrow'", "c": "It deletes them from the sentence", "d": "It translates them into numbers"}, "ans": "a"},
        {"q": "What is the difference between a 'physical change' and a 'chemical change'?", "opts": {"a": "A physical change does not produce a new substance (like ice melting), while a chemical change does (like soda reacting with acid)", "b": "Chemical changes are always reversible, physical changes are not", "c": "Physical changes only occur in solids, chemical changes in gases", "d": "There is no difference; they are synonyms"}, "ans": "a"},
        {"q": "Which prefix can be added to the word 'toxic' to mean non-poisonous?", "opts": {"a": "non- (nontoxic)", "b": "un-", "c": "im-", "d": "de-"}, "ans": "a"},
        {"q": "Complete: The father asked his son where he _____ his textbook.", "opts": {"a": "had put", "b": "puts", "c": "will put", "d": "is putting"}, "ans": "a"},
        {"q": "Identify the modal verb of possibility in the sentence: 'It might rain later, so keep the soda dry.'", "opts": {"a": "might", "b": "rain", "c": "keep", "d": "dry"}, "ans": "a"},
        {"q": "What is the past tense of the verb 'shake' when mixing a liquid compound?", "opts": {"a": "shook", "b": "shaked", "c": "shaken", "d": "shakes"}, "ans": "a"},
        {"q": "What does a chemical 'reaction' typically produce?", "opts": {"a": "A change in energy, gas release, or formation of a new substance", "b": "A new element only", "c": "An increase in volume without weight change", "d": "A primary key constraint in database"}, "ans": "a"},
        {"q": "Which word is a synonym for 'sibling'?", "opts": {"a": "brother or sister", "b": "parent", "c": "cousin", "d": "uncle"}, "ans": "a"},
        {"q": "Complete: The teacher asked us if we _____ the experiment.", "opts": {"a": "had completed", "b": "completing", "c": "will complete", "d": "are completing"}, "ans": "a"},
        {"q": "What is the past participle of 'drink' when talking about soda?", "opts": {"a": "drunk", "b": "drank", "c": "drinked", "d": "drinking"}, "ans": "a"},
        {"q": "Identify the modal verb showing recommendation in: 'We should study chemical bonds today.'", "opts": {"a": "should", "b": "study", "c": "chemical", "d": "bonds"}, "ans": "a"},
        {"q": "What does the word 'solution' mean in chemistry?", "opts": {"a": "A liquid mixture in which the minor component is uniformly distributed within the major component", "b": "The answer to a mathematical equation", "c": "A legal settlement between family members", "d": "A database configuration setting"}, "ans": "a"},
        {"q": "Which of these is a homophone for the word 'weak'?", "opts": {"a": "week", "b": "woke", "c": "walk", "d": "wick"}, "ans": "a"},
        {"q": "Identify the correct indirect speech: 'My son said, \"I finished my homework.\"'", "opts": {"a": "My son said that he had finished his homework.", "b": "My son said that he finished my homework.", "c": "My son said that I had finished his homework.", "d": "My son said he has finished his homework."}, "ans": "a"},
        {"q": "What is the meaning of the word 'react' in chemistry?", "opts": {"a": "To undergo a chemical change with another substance", "b": "To answer a father's question quickly", "c": "To freeze a liquid substance", "d": "To write code inside a file"}, "ans": "a"},
        {"q": "Complete: He asked me if I _____ help him carry the chemical solutions.", "opts": {"a": "could", "b": "can", "c": "shall", "d": "will"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Which of the following sentences correctly demonstrates the conversion of a direct question into indirect speech?", "opts": {"a": "The father asked his son why he had not dissolved the baking soda.", "b": "The father asked his son why did you not dissolve the baking soda?", "c": "The father asked his son that why he had not dissolved the baking soda.", "d": "The father asked his son why he did not dissolve the baking soda?"}, "ans": "a"},
        {"q": "In chemical nomenclature, how does 'sodium bicarbonate' (edible soda) differ structurally from 'sodium carbonate' (washing soda)?", "opts": {"a": "Sodium bicarbonate contains a hydrogen atom in its molecular structure, whereas sodium carbonate does not", "b": "Sodium carbonate has no carbon atoms", "c": "Sodium bicarbonate is a liquid, sodium carbonate is a gas", "d": "There is no chemical difference between them"}, "ans": "a"},
        {"q": "Analyze the syntax: 'He proposed that we should dissolve the compound immediately.' What subjunctive construction is demonstrated here?", "opts": {"a": "Mandative subjunctive using a modal auxiliary", "b": "Past subjunctive of possibility", "c": "Infinitive clause of purpose", "d": "Gerund construction"}, "ans": "a"},
        {"q": "Which sentence contains a modal verb expressing a 'high logical probability' or deduction?", "opts": {"a": "The white powder must be baking soda because it reacted with the lemon juice.", "b": "You must wash your hands after handling chemical compounds.", "c": "He must not visit the laboratory without permission.", "d": "We must study tenses for our English exam."}, "ans": "a"},
        {"q": "What is the meaning of the word 'insoluble'?", "opts": {"a": "incapable of being dissolved in a liquid solvent", "b": "easy to explain in a family talk", "c": "extremely expensive to buy in Somalia", "d": "referring to a gas state"}, "ans": "a"},
        {"q": "Identify the correct indirect speech for: 'The chemist asked, \"Which compound did you test yesterday?\"'", "opts": {"a": "The chemist asked which compound I had tested the day before.", "b": "The chemist asked which compound did I test yesterday.", "c": "The chemist asked that which compound I tested yesterday.", "d": "The chemist asked which compound had I tested the day before."}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'cereal' (grain food)?", "opts": {"a": "serial (arranged in a series)", "b": "seal", "c": "soul", "d": "cellar"}, "ans": "a"},
        {"q": "In family relations, the term 'filial piety' refers to:", "opts": {"a": "the duty, respect, and obedience of a son or daughter to their parents", "b": "the legal ownership of a family house", "c": "the chemical analysis of water", "d": "the language skills of grandparents"}, "ans": "a"},
        {"q": "What is the past subjunctive form of the verb 'be' used in conditional clauses of imagination, such as: 'If he _____ my son, I would advise him differently.'?", "opts": {"a": "were", "b": "was", "c": "been", "d": "be"}, "ans": "a"},
        {"q": "Which chemical process explains the release of gas bubbles when baking soda is heated?", "opts": {"a": "Thermal decomposition", "b": "Physical dissolution", "c": "Sublimation", "d": "Condensation"}, "ans": "a"},
        {"q": "Identify the suffix that can be added to the noun 'parent' to mean the state of being a parent.", "opts": {"a": "-hood (parenthood)", "b": "-ship", "c": "-ment", "d": "-ness"}, "ans": "a"},
        {"q": "Which sentence contains a non-defining relative clause identifying a chemical substance?", "opts": {"a": "Sodium bicarbonate, which is commonly called baking soda, is a white crystalline solid.", "b": "Sodium bicarbonate which is commonly called baking soda is a white crystalline solid.", "c": "Sodium bicarbonate is a white crystalline solid which is called baking soda.", "d": "Being called baking soda, sodium bicarbonate is a white crystalline solid."}, "ans": "a"},
        {"q": "What is the past participle form of 'cast'?", "opts": {"a": "cast", "b": "casted", "c": "casting", "d": "casts"}, "ans": "a"},
        {"q": "A chemical solution that has dissolved the maximum amount of solute at a given temperature is said to be:", "opts": {"a": "saturated", "b": "unsaturated", "c": "diluted", "d": "insoluble"}, "ans": "a"},
        {"q": "Which word is a synonym for 'domestic' in the context of household activities?", "opts": {"a": "household or familial", "b": "foreign", "c": "wild", "d": "industrial"}, "ans": "a"},
        {"q": "Complete the reported speech: The father asked his son where he _____ the previous night.", "opts": {"a": "had been", "b": "was", "c": "is", "d": "has been"}, "ans": "a"},
        {"q": "Which of these pairs represents homophones with different spellings?", "opts": {"a": "knead / need", "b": "knit / knot", "c": "knife / knave", "d": "knows / nose (Wait, knobs / nobs)"}, "ans": "a"},
        {"q": "What punctuation marks are used to enclose the exact words of a speaker in direct speech?", "opts": {"a": "Quotation marks", "b": "Parentheses", "c": "Semicolons", "d": "Dashes"}, "ans": "a"},
        {"q": "When a reporting verb is in the future tense (e.g. 'He will say'), what tense shift occurs in indirect speech?", "opts": {"a": "No tense shift occurs", "b": "The tense shifts to simple past", "c": "The tense shifts to past perfect", "d": "The tense changes to future perfect"}, "ans": "a"},
        {"q": "What is the antonym of the chemical term 'acidic'?", "opts": {"a": "alkaline or basic", "b": "neutral", "c": "salty", "d": "toxic"}, "ans": "a"},
        {"q": "Which sentence is grammatically correct in reported speech?", "opts": {"a": "He asked me if I had seen his chemical solution.", "b": "He asked me that if I had seen his chemical solution.", "c": "He asked me had I seen his chemical solution.", "d": "He asked me did I see his chemical solution."}, "ans": "a"},
        {"q": "What is the chemical symbol for Sodium?", "opts": {"a": "Na", "b": "So", "c": "S", "d": "N"}, "ans": "a"},
        {"q": "Which word means 'to separate a liquid from a solid by pouring it off gently'?", "opts": {"a": "decant", "b": "dissolve", "c": "filter", "d": "evaporate"}, "ans": "a"},
        {"q": "Identify the modal verb showing obligation in: 'You must not inhale the chemical gases.'", "opts": {"a": "must", "b": "inhale", "c": "chemical", "d": "not"}, "ans": "a"},
        {"q": "What does the suffix '-ify' mean in words like 'solidify' or 'purify'?", "opts": {"a": "to make or cause to become", "b": "full of", "c": "without", "d": "study of"}, "ans": "a"},
        {"q": "Convert to direct speech: 'He told me that he would help me.'", "opts": {"a": "He said, \"I will help you.\"", "b": "He said, \"I would help you.\"", "c": "He said, \"He will help me.\"", "d": "He said, \"I will help him.\""}, "ans": "a"},
        {"q": "Which of these represents a mixture rather than a pure chemical compound?", "opts": {"a": "Air", "b": "Water", "c": "Carbon dioxide", "d": "Baking soda"}, "ans": "a"},
        {"q": "What is the past tense of 'spin' in a lab centrifuge?", "opts": {"a": "spun", "b": "spinned", "c": "span", "d": "spins"}, "ans": "a"},
        {"q": "Identify the prefix in 'decomposition'.", "opts": {"a": "de- (meaning separation or reversal)", "b": "dec-", "c": "com-", "d": "position"}, "ans": "a"},
        {"q": "What is the grammatical term for the word 'whether' in: 'He asked whether the father was home.'?", "opts": {"a": "Subordinating conjunction introducing a noun clause", "b": "Relative pronoun", "c": "Adverb of time", "d": "Coordinating conjunction"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch5_questions():
    # Chapter 5: Unit 9 & 10 (The Motherless Girl & Societies In The Past)
    # Focus: Traditional Narratives, Historical Societies, Archeological terms, Past Perfect Tense, Adverbs.
    easy = [
        {"q": "What is the term for a story that has been told for a long time, often explaining historical events or beliefs?", "opts": {"a": "Traditional narrative or legend", "b": "Scientific paper", "c": "Business proposal", "d": "Keyboard layout manual"}, "ans": "a"},
        {"q": "In the story 'The Motherless Girl', the main character is:", "opts": {"a": "An orphan girl facing hardships from a cruel stepmother", "b": "A wealthy merchant in a colossal house", "c": "A modern scientist studying plastic", "d": "A lion with a thorn in its paw"}, "ans": "a"},
        {"q": "Which tense is used to describe an action that was completed before another action in the past?", "opts": {"a": "Past perfect tense", "b": "Simple past tense", "c": "Present perfect tense", "d": "Past continuous tense"}, "ans": "a"},
        {"q": "What is the study of human history through the excavation of sites and analysis of physical remains?", "opts": {"a": "Archaeology", "b": "Biology", "c": "Chemistry", "d": "Geography"}, "ans": "a"},
        {"q": "Identify the past perfect verb form in the list below.", "opts": {"a": "had gone", "b": "went", "c": "has gone", "d": "was going"}, "ans": "a"},
        {"q": "What do we call the remains of a building or city that has been destroyed over time?", "opts": {"a": "Ruins", "b": "Mansion", "c": "Foundation", "d": "Attic"}, "ans": "a"},
        {"q": "Which of these words is an adverb of time?", "opts": {"a": "yesterday", "b": "slowly", "c": "behind", "d": "very"}, "ans": "a"},
        {"q": "Complete: Before she arrived, they _____ already left.", "opts": {"a": "had", "b": "have", "c": "did", "d": "were"}, "ans": "a"},
        {"q": "Who is a woman married to one's father after the divorce or death of one's mother?", "opts": {"a": "Stepmother", "b": "Aunt", "c": "Grandmother", "d": "Sister"}, "ans": "a"},
        {"q": "What is the synonym of the word 'ancient'?", "opts": {"a": "very old or historical", "b": "brand new", "c": "colossal", "d": "dilapidated"}, "ans": "a"},
        {"q": "In 'Societies In The Past', we study how ancient people lived and built their:", "opts": {"a": "cultures and structures", "b": "internet networks", "c": "modern packaging systems", "d": "chemical laboratories"}, "ans": "a"},
        {"q": "Which of these is an adverb of manner?", "opts": {"a": "gently", "b": "tomorrow", "c": "inside", "d": "extremely"}, "ans": "a"},
        {"q": "Complete: By the time the archaeologist arrived, the ruins _____ excavated.", "opts": {"a": "had been", "b": "were", "c": "has been", "d": "are"}, "ans": "a"},
        {"q": "What is a child whose parents are dead called?", "opts": {"a": "Orphan", "b": "Sibling", "c": "Infant", "d": "Parent"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'past'?", "opts": {"a": "passed", "b": "pest", "c": "post", "d": "pasta"}, "ans": "a"},
        {"q": "What is the past participle of 'fly'?", "opts": {"a": "flown", "b": "flew", "c": "flied", "d": "flying"}, "ans": "a"},
        {"q": "Identify the adverb in: 'The girl wept silently.'", "opts": {"a": "silently", "b": "girl", "c": "wept", "d": "the"}, "ans": "a"},
        {"q": "What does a stepmother traditionally represent in classical folklore?", "opts": {"a": "Cruelty, jealousy, and favoritism", "b": "Extreme kindness and care", "c": "Scientific knowledge", "d": "Industrial development"}, "ans": "a"},
        {"q": "Which tense is used in: 'He had studied the history of Somalia.'?", "opts": {"a": "Past perfect", "b": "Present perfect", "c": "Simple past", "d": "Future perfect"}, "ans": "a"},
        {"q": "What is a synonym of the word 'ruin'?", "opts": {"a": "destroy or wreck", "b": "build", "c": "improve", "d": "nurture"}, "ans": "a"},
        {"q": "Complete: The ancient society _____ collapsed due to severe drought.", "opts": {"a": "had", "b": "has", "c": "was", "d": "did"}, "ans": "a"},
        {"q": "Identify the adverb of place in: 'The ruins are located nearby.'", "opts": {"a": "nearby", "b": "ruins", "c": "located", "d": "are"}, "ans": "a"},
        {"q": "What do we call objects made by humans in the past, discovered by archaeologists?", "opts": {"a": "Artifacts", "b": "Compounds", "c": "Ruins", "d": "Stanzas"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "In the past perfect tense, what auxiliary verb is always paired with the past participle of the main verb?", "opts": {"a": "had", "b": "have", "c": "has", "d": "was"}, "ans": "a"},
        {"q": "Which of the following sentences correctly demonstrates the past perfect tense used alongside the simple past tense?", "opts": {"a": "When the stepmother arrived, the motherless girl had already cleaned the house.", "b": "When the stepmother had arrived, the motherless girl cleaned the house.", "c": "When the stepmother arrived, the motherless girl was already cleaning the house.", "d": "When the stepmother arrives, the motherless girl had cleaned the house."}, "ans": "a"},
        {"q": "What is the primary objective of archaeological excavations of ancient societies?", "opts": {"a": "To uncover material culture and physical remains to reconstruct past human lifestyles", "b": "To print textbooks quickly", "c": "To find oil fields for fossil fuels", "d": "To test chemical compounds like soda"}, "ans": "a"},
        {"q": "Which adverb best describes how an archaeologist would handle fragile ancient artifacts?", "opts": {"a": "meticulously or carefully", "b": "recklessly", "c": "hastily", "d": "noisily"}, "ans": "a"},
        {"q": "In 'The Motherless Girl', what did the stepmother order the girl to do to cause her distress?", "opts": {"a": "Difficult or impossible tasks, such as washing black sheep until they turned white", "b": "Reciting a poetry guide perfectly in English", "c": "Excavating an archaeological site in Egypt", "d": "Mixing chemical solutions in a lab"}, "ans": "a"},
        {"q": "Which word is a synonym for 'orphanage'?", "opts": {"a": "home for parentless children", "b": "school laboratory", "c": "mansion", "d": "city referral hospital"}, "ans": "a"},
        {"q": "How does the past perfect tense differ semantically from the simple past tense?", "opts": {"a": "The past perfect refers to a time prior to another point in the past, while the simple past refers to a general completed past action", "b": "The simple past is only used for written stories, past perfect for speech", "c": "Past perfect is used for future expectations", "d": "There is no semantic difference"}, "ans": "a"},
        {"q": "Complete: The archaeologist, who _____ ancient languages for years, easily deciphered the inscription.", "opts": {"a": "had studied", "b": "studies", "c": "is studying", "d": "will study"}, "ans": "a"},
        {"q": "What is the antonym of the word 'ancient'?", "opts": {"a": "modern or contemporary", "b": "dilapidated", "c": "colossal", "d": "traditional"}, "ans": "a"},
        {"q": "Which of these words is an adverb of degree?", "opts": {"a": "extremely", "b": "yesterday", "c": "outside", "d": "slowly"}, "ans": "a"},
        {"q": "What is the historical significance of the ancient ruins of Zeila or Taleh in Somali history?", "opts": {"a": "They represent rich historical trade, culture, and resistance societies of the past", "b": "They are modern industrial packaging plants", "c": "They are chemical laboratories", "d": "They have no historical significance"}, "ans": "a"},
        {"q": "Which suffix can be added to the adjective 'cruel' to make it a noun?", "opts": {"a": "-ty (cruelty)", "b": "-ness", "c": "-ment", "d": "-ly"}, "ans": "a"},
        {"q": "Identify the relative pronoun in: 'The artifacts that were found in the cave date back to the Stone Age.'", "opts": {"a": "that", "b": "found", "c": "cave", "d": "date"}, "ans": "a"},
        {"q": "Which word refers to the scientific study of ancient human societies based on written records?", "opts": {"a": "Historiography", "b": "Archaeology", "c": "Folkloristics", "d": "Sociology"}, "ans": "a"},
        {"q": "What is the meaning of the adverb 'hitherto'?", "opts": {"a": "until this time; up to now", "b": "in that place", "c": "very fast", "d": "loudly"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'hour'?", "opts": {"a": "our", "b": "hair", "c": "her", "d": "oar"}, "ans": "a"},
        {"q": "Complete: By the time the villagers arrived, the stepmother _____ the motherless girl to leave the village.", "opts": {"a": "had forced", "b": "forces", "c": "is forcing", "d": "will force"}, "ans": "a"},
        {"q": "Which descriptive adverb fits a historical researcher working on old scripts?", "opts": {"a": "patiently", "b": "loudly", "c": "angrily", "d": "carelessly"}, "ans": "a"},
        {"q": "What is 'folklore'?", "opts": {"a": "The traditional beliefs, customs, and stories of a community passed through oral tradition", "b": "The study of modern chemical elements", "c": "A list of rules for public presentations", "d": "The user interface design of an application"}, "ans": "a"},
        {"q": "Which sentence contains a correctly positioned adverb of frequency?", "opts": {"a": "The ancient peoples always celebrated the harvest season.", "b": "The ancient peoples celebrated always the harvest season.", "c": "Always the ancient peoples celebrated the harvest season.", "d": "The ancient peoples celebrated the harvest season always."}, "ans": "a"},
        {"q": "Which word is a synonym for 'excavate'?", "opts": {"a": "unearth or dig up", "b": "bury", "c": "construct", "d": "destroy"}, "ans": "a"},
        {"q": "Identify the word containing a prefix meaning 'former' that describes a relationship.", "opts": {"a": "ex-stepmother", "b": "sub-family", "c": "pre-society", "d": "de-family"}, "ans": "a"},
        {"q": "Complete: The ancient ruins _____ discovered by chance in the middle of the desert.", "opts": {"a": "were", "b": "had", "c": "have", "d": "did"}, "ans": "a"},
        {"q": "Which adverb describes a narrative told in a highly dramatic way?", "opts": {"a": "passionately", "b": "monotonously", "c": "briefly", "d": "silently"}, "ans": "a"},
        {"q": "What is the past perfect tense of 'see'?", "opts": {"a": "had seen", "b": "has seen", "c": "was seeing", "d": "saw"}, "ans": "a"},
        {"q": "In a traditional narrative, the pattern of events that make up the story is called the:", "opts": {"a": "plot", "b": "theme", "c": "climax", "d": "setting"}, "ans": "a"},
        {"q": "Which word is a homophone of the word 'herd' (group of animals)?", "opts": {"a": "heard (perceived sound)", "b": "hard", "c": "head", "d": "hood"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Which of the following sentences correctly utilizes the past perfect passive construction?", "opts": {"a": "Before the museum opened, the ancient artifact had been restored by the experts.", "b": "Before the museum opened, the experts had restored the ancient artifact.", "c": "Before the museum opened, the ancient artifact was restored by the experts.", "d": "Before the museum opened, the ancient artifact had restored by the experts."}, "ans": "a"},
        {"q": "In historiography, what is the critical difference between 'primary sources' and 'secondary sources' regarding societies in the past?", "opts": {"a": "Primary sources are direct first-hand testimonies from the time, while secondary sources are subsequent analyses by historians", "b": "Primary sources are written in English, secondary in Somali", "c": "Primary sources are older than 1000 years, secondary sources are newer", "d": "There is no difference in their historical validity"}, "ans": "a"},
        {"q": "Analyze the syntax: 'No sooner had the girl wept than a magical helper appeared in the forest.' What grammatical construction is demonstrated here?", "opts": {"a": "Negative inversion indicating rapid successive events", "b": "Subjunctive mood of regret", "c": "Relative clause of time", "d": "Participle phrase"}, "ans": "a"},
        {"q": "Which sentence contains an adverb acting as a sentence modifier (disjunct)?", "opts": {"a": "Fortunately, the archaeologist discovered the ruins before they were vandalized.", "b": "The archaeologist fortunately discovered the ruins before they were vandalized.", "c": "The archaeologist discovered the ruins fortunately before they were vandalized.", "d": "The ruins were fortunately discovered by the archaeologist."}, "ans": "a"},
        {"q": "What does the 'cruel stepmother' motif symbolize in psychoanalytic analysis of folktales?", "opts": {"a": "The child's psychological split between the nurturing mother and the punishing, demanding authority figure", "b": "Historical struggles between different clans in ancient societies", "c": "Lack of legal laws in traditional villages", "d": "The struggle for clean water in rural areas"}, "ans": "a"},
        {"q": "Which of the following is a subordinating conjunction of cause used in narratives?", "opts": {"a": "inasmuch as", "b": "provided that", "c": "even though", "d": "so that"}, "ans": "a"},
        {"q": "What does the word 'relic' mean in archaeological contexts?", "opts": {"a": "an object surviving from an earlier time, especially one of historical interest", "b": "a modern tool used to dig up ruins", "c": "a list of museum rules", "d": "a chemical compound"}, "ans": "a"},
        {"q": "Complete the sentence: If the motherless girl _____ the magical helper's advice, she would have failed the stepmother's test.", "opts": {"a": "had not followed", "b": "did not follow", "c": "would not follow", "d": "has not followed"}, "ans": "a"},
        {"q": "Identify the conjunctive adverb in: 'The ruins were buried under sand; consequently, they remained preserved for centuries.'", "opts": {"a": "consequently", "b": "were buried", "c": "remained", "d": "preserved"}, "ans": "a"},
        {"q": "What is the past participle form of the irregular verb 'tread'?", "opts": {"a": "trodden", "b": "treaded", "c": "trod", "d": "treading"}, "ans": "a"},
        {"q": "In historical research, the term 'chronology' refers to:", "opts": {"a": "the arrangement of events or dates in the order of their occurrence", "b": "the study of ancient tools and weapons", "c": "the translation of oral stories to english", "d": "the grammar of the past perfect tense"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'cent' (money coin)?", "opts": {"a": "scent (smell) or sent (past tense of send)", "b": "sentient", "c": "saint", "d": "sound"}, "ans": "a"},
        {"q": "What is the past perfect tense of 'slay'?", "opts": {"a": "had slain", "b": "had slayed", "c": "had slew", "d": "had slaying"}, "ans": "a"},
        {"q": "Which sentence contains a correctly punctuated parenthetical adverbial phrase?", "opts": {"a": "The artifact, as it turned out, was a fake.", "b": "The artifact as it turned out was a fake.", "c": "The artifact, as it turned out was a fake.", "d": "The artifact as it turned, out was a fake."}, "ans": "a"},
        {"q": "What is the term for the process of determining the age of an organic object by measuring its carbon-14 content?", "opts": {"a": "Radiocarbon dating", "b": "Archaeological excavation", "c": "Chronological sequencing", "d": "Chemical analysis"}, "ans": "a"},
        {"q": "Which word is a synonym for 'veneration' (respect)?", "opts": {"a": "reverence or deep respect", "b": "disdain", "c": "cruelty", "d": "neglect"}, "ans": "a"},
        {"q": "What is the past perfect tense of the irregular verb 'weep'?", "opts": {"a": "had wept", "b": "had weeped", "c": "had weeping", "d": "had weeps"}, "ans": "a"},
        {"q": "In the sentence: 'The archaeologist worked tirelessly lest the impending rains should destroy the trenches', what is 'lest' indicating?", "opts": {"a": "prevention of a feared outcome", "b": "a reason for working", "c": "a time sequence", "d": "a comparison"}, "ans": "a"},
        {"q": "Which of the following is a key feature of 'traditional narrative structure'?", "opts": {"a": "An introduction, rising conflict, a clear climax, falling action, and a moral resolution", "b": "A list of definitions and vocabulary exercises chronologically", "c": "A set of questions and answers about chemistry", "d": "A table of contents and outlines"}, "ans": "a"},
        {"q": "Complete the proverb: Necessity is the mother of _____.", "opts": {"a": "invention", "b": "patience", "c": "learning", "d": "wisdom"}, "ans": "a"},
        {"q": "What is the past perfect tense of 'cling'?", "opts": {"a": "had clung", "b": "had clinged", "c": "had clang", "d": "had clings"}, "ans": "a"},
        {"q": "Identify the adverb of manner that modifies another adverb in: 'The scholar translated the ancient tablet quite easily.'", "opts": {"a": "quite", "b": "easily", "c": "translated", "d": "ancient"}, "ans": "a"},
        {"q": "What is the synonym of the word 'remnants'?", "opts": {"a": "remaining parts or relics", "b": "grand structures", "c": "modern tools", "d": "future designs"}, "ans": "a"},
        {"q": "Complete: No sooner had the ancient scroll been opened _____ it began to crumble in the fresh air.", "opts": {"a": "than", "b": "then", "c": "when", "d": "before"}, "ans": "a"},
        {"q": "What is the past perfect tense of 'rise'?", "opts": {"a": "had risen", "b": "had rose", "c": "had rised", "d": "had rising"}, "ans": "a"},
        {"q": "In literary terminology, the historical context, physical location, and social environment of a narrative is called the:", "opts": {"a": "setting", "b": "plot", "c": "conflict", "d": "theme"}, "ans": "a"},
        {"q": "Which adverb of time refers to 'immediately after that'?", "opts": {"a": "thereupon", "b": "hitherto", "c": "henceforth", "d": "formerly"}, "ans": "a"},
        {"q": "What is the past perfect tense of 'stride'?", "opts": {"a": "had stridden", "b": "had strode", "c": "had strided", "d": "had striding"}, "ans": "a"},
        {"q": "Identify the suffix that can be added to the adjective 'ancient' to make it a noun.", "opts": {"a": "-ty (ancientry)", "b": "-ness", "c": "-ment", "d": "-ship"}, "ans": "a"},
        {"q": "What grammatical structure is used in: 'Had they not excavated the ruins, the artifacts would have been lost.'?", "opts": {"a": "Inverted conditional clause (third conditional)", "b": "Gerund phrase", "c": "Past continuous passive", "d": "Noun clause"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch6_questions():
    # Chapter 6: Unit 11 & 12 (Nature Conservation & The Killer Plastic)
    # Focus: Environmental terms, Plastic Pollution, Conservation, Modal Verbs (should, must, have to), Conditionals.
    easy = [
        {"q": "What is 'nature conservation'?", "opts": {"a": "The protection and preservation of the natural environment and wildlife", "b": "The factory production of plastic bags", "c": "The design of building architectures", "d": "The chemistry of baking soda"}, "ans": "a"},
        {"q": "Why is plastic referred to as 'The Killer Plastic' in Unit 12?", "opts": {"a": "Because it pollutes the environment and kills marine and domestic animals when ingested", "b": "Because it is an active chemical explosive", "c": "Because it makes loud roaring sounds", "d": "Because it dissolves easily in water"}, "ans": "a"},
        {"q": "Which modal verb is commonly used to express a strong rule or duty?", "opts": {"a": "must", "b": "might", "c": "could", "d": "would"}, "ans": "a"},
        {"q": "What type of conditional sentence is used to express general truths (e.g. 'If you heat ice, it melts')?", "opts": {"a": "Zero conditional", "b": "First conditional", "c": "Second conditional", "d": "Third conditional"}, "ans": "a"},
        {"q": "What is the term for converting waste materials into new materials and objects?", "opts": {"a": "Recycling", "b": "Conserving", "c": "Packaging", "d": "Polluting"}, "ans": "a"},
        {"q": "Complete the rule: We _____ throw plastic bags on the streets.", "opts": {"a": "must not", "b": "should", "c": "have to", "d": "might"}, "ans": "a"},
        {"q": "What material is made from petroleum/fossil fuels and is not easily biodegradable?", "opts": {"a": "Plastic", "b": "Wood", "c": "Paper", "d": "Cotton"}, "ans": "a"},
        {"q": "Complete: If we pollute the ocean, marine life _____ suffer.", "opts": {"a": "will", "b": "would", "c": "did", "d": "had"}, "ans": "a"},
        {"q": "Which word is a synonym of the word 'pollute'?", "opts": {"a": "contaminate or dirty", "b": "clean", "c": "conserve", "d": "protect"}, "ans": "a"},
        {"q": "What is the antonym of the word 'conservation'?", "opts": {"a": "destruction or neglect", "b": "protection", "c": "preservation", "d": "safety"}, "ans": "a"},
        {"q": "Animals that live in water are called _____ animals.", "opts": {"a": "marine", "b": "domestic", "c": "terrestrial", "d": "extinct"}, "ans": "a"},
        {"q": "Complete: You _____ to turn off the lights to save electricity.", "opts": {"a": "have", "b": "must", "c": "should", "d": "ought"}, "ans": "a"},
        {"q": "Which conditional sentence describes a future possibility (e.g. 'If it rains, we will stay home')?", "opts": {"a": "First conditional", "b": "Zero conditional", "c": "Second conditional", "d": "Third conditional"}, "ans": "a"},
        {"q": "What do we call materials like coal, oil, and natural gas formed from ancient organic remains?", "opts": {"a": "Fossil fuels", "b": "Baking sodas", "c": "Biodegradables", "d": "Recyclables"}, "ans": "a"},
        {"q": "Which modal verb shows suggestion or advice?", "opts": {"a": "should", "b": "must", "c": "have to", "d": "will"}, "ans": "a"},
        {"q": "What is the synonym of the word 'wildlife'?", "opts": {"a": "undomesticated animals and plants", "b": "city pets", "c": "plastic pollutants", "d": "farm crops"}, "ans": "a"},
        {"q": "Complete: If people _____ reusable bags, plastic waste will decrease.", "opts": {"a": "use", "b": "will use", "c": "used", "d": "are using"}, "ans": "a"},
        {"q": "What does 'non-biodegradable' mean?", "opts": {"a": "not capable of being broken down by biological processes", "b": "safe to eat or digest", "c": "dissolves quickly in water", "d": "reusable for cooking"}, "ans": "a"},
        {"q": "Identify the modal verb in: 'We must protect our ecosystems.'", "opts": {"a": "must", "b": "protect", "c": "our", "d": "ecosystems"}, "ans": "a"},
        {"q": "What is the main danger of plastic bags to livestock (cows, goats)?", "opts": {"a": "They eat them by mistake, causing stomach blockage and death", "b": "They are afraid of their colors", "c": "They cut their hooves on them", "d": "There is no danger"}, "ans": "a"},
        {"q": "Which of these is a homophone for the word 'waste'?", "opts": {"a": "waist", "b": "west", "c": "wet", "d": "worst"}, "ans": "a"},
        {"q": "Identify the conditional conjunction in: 'If we plant trees, the air becomes cleaner.'", "opts": {"a": "If", "b": "plant", "c": "cleaner", "d": "becomes"}, "ans": "a"},
        {"q": "Which word describes a place where trash is officially dumped?", "opts": {"a": "landfill or dump", "b": "forest", "c": "attic", "d": "villa"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "What is the primary difference in meaning between the modal verbs 'must' and 'should'?", "opts": {"a": "'Must' expresses a strong obligation or absolute necessity, whereas 'should' expresses a recommendation or advice", "b": "'Should' is past tense, 'must' is present tense", "c": "'Must' is informal, 'should' is formal", "d": "There is no difference; they are exact synonyms"}, "ans": "a"},
        {"q": "Which of the following represents a second conditional sentence (expressing imaginary or unlikely situations)?", "opts": {"a": "If we banned plastic bags, our streets would be cleaner.", "b": "If we ban plastic bags, our streets will be cleaner.", "c": "If we ban plastic bags, our streets are cleaner.", "d": "If we had banned plastic bags, our streets would have been cleaner."}, "ans": "a"},
        {"q": "Why are single-use plastic bags a severe threat to marine ecosystems?", "opts": {"a": "They resemble food (like jellyfish) to marine creatures, leading to ingestion, choking, and death", "b": "They dissolve and turn the water acidic", "c": "They make the ocean water boil", "d": "They block the solar panels in the sea"}, "ans": "a"},
        {"q": "Which verb is used in: 'We don't have to pay for the garbage bags; they are free.'?", "opts": {"a": "don't have to (expressing absence of obligation)", "b": "must not (expressing prohibition)", "c": "should not (expressing advice)", "d": "might not (expressing doubt)"}, "ans": "a"},
        {"q": "Complete: If we _____ fossil fuels at the current rate, global temperatures will continue to rise.", "opts": {"a": "burn", "b": "burned", "c": "will burn", "d": "had burned"}, "ans": "a"},
        {"q": "What does 'ecological balance' refer to?", "opts": {"a": "A state of dynamic equilibrium within a community of organisms in which genetic, species and ecosystem diversity remain relatively stable", "b": "Comparing the weight of animals in a forest", "c": "The pricing of plastic recycling plants", "d": "Determining primary keys for databases"}, "ans": "a"},
        {"q": "Which modal verb is best for expressing a prohibition in: 'You _____ dump toxic chemical waste in the river.'?", "opts": {"a": "must not", "b": "don't have to", "c": "ought to", "d": "should not have"}, "ans": "a"},
        {"q": "Complete: If you _____ an animal in danger, what would you do?", "opts": {"a": "saw", "b": "see", "c": "will see", "d": "had seen"}, "ans": "a"},
        {"q": "What is the synonym of the word 'conservationist'?", "opts": {"a": "a person who advocates for the protection of the environment", "b": "a factory owner who produces plastic bags", "c": "an archaeologist studying ruins", "d": "a doctor who treats allergies"}, "ans": "a"},
        {"q": "Which of the following sentences contains a conditional clause of condition?", "opts": {"a": "Unless we take immediate action, the plastic pollution will overwhelm our shores.", "b": "We must take immediate action because the shores are polluted.", "c": "We took immediate action to clean our shores.", "d": "Taking immediate action is good for the environment."}, "ans": "a"},
        {"q": "What grammatical error is in: 'If I was you, I would stop using single-use plastic bottles.'?", "opts": {"a": "Use of 'was' instead of subjunctive 'were' in second conditional ('If I were you')", "b": "Spelling of 'plastic'", "c": "Use of conditional auxiliary 'would'", "d": "Punctuation mark at the end"}, "ans": "a"},
        {"q": "Which conjunction is synonymous with 'if not' in conditional sentences?", "opts": {"a": "unless", "b": "provided", "c": "although", "d": "because"}, "ans": "a"},
        {"q": "What is the past tense of the verb 'throw' when referring to litter?", "opts": {"a": "threw", "b": "thrown", "c": "throwed", "d": "throwing"}, "ans": "a"},
        {"q": "In environmental science, what is 'biodiversity'?", "opts": {"a": "The variety of plant and animal life in a particular habitat", "b": "The chemical breakdown of plastic bags", "c": "The amount of waste in a landfill", "d": "The states of matter in a chemical solution"}, "ans": "a"},
        {"q": "Complete the sentence: Local authorities _____ implement stricter recycling policies to tackle plastic waste.", "opts": {"a": "ought to", "b": "might to", "c": "must to", "d": "would to"}, "ans": "a"},
        {"q": "Identify the modal verb of obligation in: 'Citizens have to separate recyclable materials from organic waste.'", "opts": {"a": "have to", "b": "separate", "c": "materials", "d": "organic"}, "ans": "a"},
        {"q": "What is the past tense of 'burn'?", "opts": {"a": "burned or burnt", "b": "burning", "c": "burns", "d": "burn"}, "ans": "a"},
        {"q": "What does the word 'contamination' mean in environmental contexts?", "opts": {"a": "the action of making something impure or dirty by exposing it to pollutants", "b": "the process of planting trees", "c": "the recycling of plastic bottles", "d": "the protection of wildlife"}, "ans": "a"},
        {"q": "Which of these is a homophone for the word 'allowed'?", "opts": {"a": "aloud", "b": "alloyed", "c": "allied", "d": "alowed"}, "ans": "a"},
        {"q": "Complete the first conditional: If we do not reduce plastic usage, the landfills _____ overflow.", "opts": {"a": "will", "b": "would", "c": "do", "d": "shall"}, "ans": "a"},
        {"q": "What is the past tense of 'bleed'?", "opts": {"a": "bled", "b": "bleeded", "c": "bleeding", "d": "bleeds"}, "ans": "a"},
        {"q": "Identify the conditional clause in: 'We will save the forest if we ban logging.'", "opts": {"a": "if we ban logging", "b": "We will save the forest", "c": "We will save", "d": "if we ban"}, "ans": "a"},
        {"q": "What is the synonym of the word 'deplete'?", "opts": {"a": "exhaust or reduce drastically", "b": "fill", "c": "conserve", "d": "create"}, "ans": "a"},
        {"q": "Complete: If you _____ garbage in the ocean, it harms fish.", "opts": {"a": "throw", "b": "threw", "c": "will throw", "d": "thrown"}, "ans": "a"},
        {"q": "What is the past tense of 'drink' in: 'The goat drank polluted water.'?", "opts": {"a": "drank", "b": "drunk", "c": "drinked", "d": "drinking"}, "ans": "a"},
        {"q": "In grammar, modal verbs are auxiliary verbs that express:", "opts": {"a": "necessity, possibility, permission, or obligation", "b": "actions completed in the past", "c": "descriptions of colossal structures", "d": "rhyme schemes of poems"}, "ans": "a"},
        {"q": "Which word is a homophone of the word 'bare'?", "opts": {"a": "bear", "b": "beer", "c": "bar", "d": "bore"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Which of the following sentences correctly utilizes a third conditional structure to express past regret about the environment?", "opts": {"a": "If we had banned single-use plastics twenty years ago, our marine life would have recovered.", "b": "If we banned single-use plastics twenty years ago, our marine life would recover.", "c": "If we had banned single-use plastics twenty years ago, our marine life would recover.", "d": "If we banned single-use plastics twenty years ago, our marine life would have recovered."}, "ans": "a"},
        {"q": "In conservation ecology, what is the concept of a 'carbon footprint'?", "opts": {"a": "The total amount of greenhouse gases produced to directly and indirectly support human activities", "b": "The physical print left by burning fossil fuels on trees", "c": "The amount of carbon dioxide dissolved in soda drinks", "d": "The weight of charcoal burned in traditional stoves"}, "ans": "a"},
        {"q": "Analyze the syntax: 'Should we continue to ignore nature conservation, the environmental consequences will be catastrophic.' What does 'should' represent here?", "opts": {"a": "An inverted conditional clause equivalent to 'If we should continue...'", "b": "A recommendation from a conservationist", "c": "A statement of fact", "d": "A past obligation"}, "ans": "a"},
        {"q": "Which sentence contains a modal verb expressing absolute prohibition?", "opts": {"a": "Factories must not release untreated industrial chemicals into the local river systems.", "b": "Factories do not have to release untreated chemicals into the local river systems.", "c": "Factories should not release untreated chemicals into the local river systems.", "d": "Factories might not release untreated chemicals into the local river systems."}, "ans": "a"},
        {"q": "What is the meaning of the word 'biodegradation'?", "opts": {"a": "the chemical breakdown of organic materials by physiological processes of living organisms", "b": "the process of generating plastic compounds in a lab", "c": "the sorting of garbage in a landfill", "d": "the protection of endangered species"}, "ans": "a"},
        {"q": "Identify the correct conditional sentence using 'provided that':", "opts": {"a": "We can reverse plastic pollution, provided that global communities enforce strict bans.", "b": "Provided that we can reverse plastic pollution global communities enforce strict bans.", "c": "We can reverse plastic pollution that provided global communities enforce strict bans.", "d": "Enforcing strict bans, provided that we reverse plastic pollution."}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'principal' (chief or main)?", "opts": {"a": "principle (rule or belief)", "b": "printable", "c": "princess", "d": "principality"}, "ans": "a"},
        {"q": "In environmental laws, the 'polluter pays principle' mandates that:", "opts": {"a": "the parties responsible for producing pollution must bear the costs of managing it", "b": "citizens must pay taxes to buy plastic bags", "c": "the government must pay factories to clean rivers", "d": "recorders of air quality are funded by fees"}, "ans": "a"},
        {"q": "What is the past subjunctive form of 'have' in conditional structures, such as: 'If we _____ more conservation reserves, our species would survive.'?", "opts": {"a": "had", "b": "have", "c": "has", "d": "were"}, "ans": "a"},
        {"q": "Which chemical process converts discarded plastic waste back into its raw monomer oil components?", "opts": {"a": "Pyrolysis (chemical recycling)", "b": "Thermal incineration", "c": "Biodegradation", "d": "Mechanical sorting"}, "ans": "a"},
        {"q": "Identify the suffix that can be added to the adjective 'diverse' to make it a noun.", "opts": {"a": "-sity (diversity)", "b": "-ness", "c": "-ment", "d": "-ship"}, "ans": "a"},
        {"q": "Which sentence contains a non-defining relative clause about nature conservation?", "opts": {"a": "Wildlife conservation, which requires international cooperation, faces threats from poaching.", "b": "Wildlife conservation which requires international cooperation faces threats from poaching.", "c": "Wildlife conservation is a critical practice which requires international cooperation.", "d": "Requiring international cooperation, wildlife conservation faces threats from poaching."}, "ans": "a"},
        {"q": "What is the past participle form of the irregular verb 'sow'?", "opts": {"a": "sown", "b": "sowed", "c": "sowing", "d": "sows"}, "ans": "a"},
        {"q": "A biological community of interacting organisms and their physical environment is called:", "opts": {"a": "an ecosystem", "b": "biodiversity", "c": "a biosphere", "d": "an ecology"}, "ans": "a"},
        {"q": "Which word is a synonym for 'jeopardize' in the context of conservation?", "opts": {"a": "endanger or threaten", "b": "protect", "c": "improve", "d": "assess"}, "ans": "a"},
        {"q": "Complete the conditional: Had they installed the recycling plant, they _____ thousands of tons of plastic.", "opts": {"a": "would have saved", "b": "will save", "c": "would save", "d": "shall have saved"}, "ans": "a"},
        {"q": "Which of these pairs represents homophones with different meanings?", "opts": {"a": "desert (abandon) / dessert (sweet food)", "b": "depress / compress", "c": "deforest / deface", "d": "devise / device"}, "ans": "a"},
        {"q": "What is the primary role of the 'conjunction' in combining conditional clauses?", "opts": {"a": "It establishes the logical condition relationship between the main clause and the conditional clause", "b": "It modifies the nouns in the sentence", "c": "It indicates the spelling of the verbs", "d": "It provides the pronunciation of words"}, "ans": "a"},
        {"q": "When 'must not' is used in safety guidelines, it indicates:", "opts": {"a": "absolute prohibition; it is illegal or dangerous to do this", "b": "a lack of necessity; you can choose whether to do it", "c": "a polite recommendation", "d": "a future expectation"}, "ans": "a"},
        {"q": "What is the antonym of the environmental term 'sustainable'?", "opts": {"a": "unsustainable or depleting", "b": "renewable", "c": "clean", "d": "biodegradable"}, "ans": "a"},
        {"q": "Which sentence is grammatically correct in conditional formatting?", "opts": {"a": "If we were to ban plastic bags, our environment would benefit.", "b": "If we were to ban plastic bags, our environment will benefit.", "c": "If we were to ban plastic bags, our environment would have benefited.", "d": "If we had banned plastic bags, our environment would benefit."}, "ans": "a"},
        {"q": "What is the chemical element that constitutes the backbone of all plastic polymers?", "opts": {"a": "Carbon", "b": "Oxygen", "c": "Nitrogen", "d": "Hydrogen"}, "ans": "a"},
        {"q": "Which word means 'the permanent destruction of forests in order to make the land available for other uses'?", "opts": {"a": "deforestation", "b": "reforestation", "c": "conservation", "d": "cultivation"}, "ans": "a"},
        {"q": "Identify the modal verb showing capability in: 'Microorganisms can degrade certain organic polymers over time.'", "opts": {"a": "can", "b": "degrade", "c": "certain", "d": "organic"}, "ans": "a"},
        {"q": "What does the prefix 'bio-' mean in words like 'biodegradable' or 'biosphere'?", "opts": {"a": "life or living organisms", "b": "two or double", "c": "chemical", "d": "large"}, "ans": "a"},
        {"q": "Convert to a second conditional: 'If we reduce our carbon footprint, we protect species.'", "opts": {"a": "If we reduced our carbon footprint, we would protect species.", "b": "If we reduce our carbon footprint, we will protect species.", "c": "If we had reduced our carbon footprint, we would have protected species.", "d": "If we reduce our carbon footprint, we would protect species."}, "ans": "a"},
        {"q": "Which of these represents a renewable energy resource?", "opts": {"a": "Solar energy", "b": "Petroleum", "c": "Coal", "d": "Natural gas"}, "ans": "a"},
        {"q": "What is the past tense of 'wind' in: 'The river wound through the conservation forest.'?", "opts": {"a": "wound", "b": "winded", "c": "wand", "d": "winds"}, "ans": "a"},
        {"q": "Identify the prefix in 'biodegradable'.", "opts": {"a": "bio- (meaning life) and de- (meaning down)", "b": "bio- only", "c": "de- only", "d": "grade"}, "ans": "a"},
        {"q": "What is the grammatical term for the word 'unless' in: 'Plastic waste will remain unless we recycle it.'?", "opts": {"a": "Conditional subordinating conjunction", "b": "Relative pronoun", "c": "Coordinating conjunction", "d": "Adverb of frequency"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch7_questions():
    # Chapter 7: Unit 13 & 14 (Culture Shock & Field Work)
    # Focus: Culture Shock, Traveling, Field Work, Questionnaire structure, Research Methods, Present Perfect Tense, Prepositions.
    easy = [
        {"q": "What is 'culture shock'?", "opts": {"a": "The feeling of disorientation experienced by someone suddenly subjected to an unfamiliar culture", "b": "An electrical shock received during fieldwork", "c": "A traditional dance performance", "d": "A chemistry experiment with compounds"}, "ans": "a"},
        {"q": "What is 'fieldwork' in research?", "opts": {"a": "Practical work conducted by a researcher in the natural environment rather than in a lab", "b": "Farming and planting wheat seeds", "c": "Designing user interfaces for mobile apps", "d": "Writing poetry stanzas"}, "ans": "a"},
        {"q": "Which tense is used to link the past to the present (e.g. 'I have lived here for ten years')?", "opts": {"a": "Present perfect tense", "b": "Simple past tense", "c": "Past perfect tense", "d": "Future perfect tense"}, "ans": "a"},
        {"q": "What do we call a set of printed or written questions with a choice of answers, devised for a survey?", "opts": {"a": "Questionnaire", "b": "Report", "c": "Autobiography", "d": "Proverb"}, "ans": "a"},
        {"q": "Identify the present perfect verb form in the list below.", "opts": {"a": "has visited", "b": "visited", "c": "had visited", "d": "was visiting"}, "ans": "a"},
        {"q": "Which preposition is typically used with 'shock' in 'shocked _____ the news'?", "opts": {"a": "by or at", "b": "on", "c": "with", "d": "under"}, "ans": "a"},
        {"q": "What is a traveler visiting a place for pleasure called?", "opts": {"a": "Tourist", "b": "Researcher", "c": "Local", "d": "Orphan"}, "ans": "a"},
        {"q": "Complete the sentence: We _____ already designed the questionnaire.", "opts": {"a": "have", "b": "has", "c": "did", "d": "were"}, "ans": "a"},
        {"q": "What research method involves asking questions face-to-face with a participant?", "opts": {"a": "Interview", "b": "Observation", "c": "Questionnaire", "d": "Document review"}, "ans": "a"},
        {"q": "What is the synonym of the word 'shock'?", "opts": {"a": "surprise or startle", "b": "calm", "c": "expect", "d": "help"}, "ans": "a"},
        {"q": "In fieldwork, after collecting data, researchers write a final _____.", "opts": {"a": "report", "b": "riddle", "c": "metaphor", "d": "chemical formula"}, "ans": "a"},
        {"q": "Which preposition fits: 'He is interested _____ learning local customs.'?", "opts": {"a": "in", "b": "at", "c": "on", "d": "with"}, "ans": "a"},
        {"q": "Complete: She _____ not traveled abroad yet.", "opts": {"a": "has", "b": "have", "c": "is", "d": "was"}, "ans": "a"},
        {"q": "What do we call the facts and statistics collected together for reference or analysis?", "opts": {"a": "Data", "b": "Poem", "c": "Compound", "d": "Stanza"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'road'?", "opts": {"a": "rode", "b": "rod", "c": "rid", "d": "red"}, "ans": "a"},
        {"q": "What is the past participle of 'go'?", "opts": {"a": "gone", "b": "went", "c": "goes", "d": "going"}, "ans": "a"},
        {"q": "Identify the preposition in: 'They are walking in the field.'", "opts": {"a": "in", "b": "walking", "c": "the", "d": "field"}, "ans": "a"},
        {"q": "What is a main symptom of culture shock?", "opts": {"a": "Feeling anxious, confused, and homesick", "b": "A high biological allergy reaction", "c": "A severe physical injury", "d": "An absolute database failure"}, "ans": "a"},
        {"q": "Which tense is used in: 'I have completed my fieldwork.'?", "opts": {"a": "Present perfect", "b": "Past perfect", "c": "Simple past", "d": "Future perfect"}, "ans": "a"},
        {"q": "What is a synonym of the word 'shocking'?", "opts": {"a": "astonishing or appalling", "b": "pleasant", "c": "predicted", "d": "tiny"}, "ans": "a"},
        {"q": "Complete: The research team _____ collected sixty questionnaires.", "opts": {"a": "has", "b": "have", "c": "is", "d": "did"}, "ans": "a"},
        {"q": "Identify the preposition of time in: 'We will meet at noon.'", "opts": {"a": "at", "b": "meet", "c": "noon", "d": "will"}, "ans": "a"},
        {"q": "What do we call the people who answer questions in a survey?", "opts": {"a": "Respondents", "b": "Researchers", "c": "Authors", "d": "Orphans"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "What auxiliary verbs are used to form the present perfect tense in English?", "opts": {"a": "have and has", "b": "had", "c": "do and does", "d": "is and are"}, "ans": "a"},
        {"q": "Which of the following sentences correctly utilizes the present perfect tense with 'for' or 'since'?", "opts": {"a": "He has been in Somalia since three months.", "b": "He has been in Somalia for three months.", "c": "He was in Somalia since three months.", "d": "He has in Somalia for three months."}, "ans": "b"},
        {"q": "What is the main advantage of using questionnaires in fieldwork research?", "opts": {"a": "They allow the researcher to collect data from a large number of people efficiently", "b": "They are always written in code", "c": "They guarantee that respondents tell the truth", "d": "They don't require any printing cost"}, "ans": "a"},
        {"q": "Which preposition is correct in: 'She adapted quickly _____ the new lifestyle in Mogadishu.'?", "opts": {"a": "to", "b": "at", "c": "with", "d": "for"}, "ans": "a"},
        {"q": "Complete: The researcher, who _____ several countries, wrote an essay on culture shock.", "opts": {"a": "has visited", "b": "visits", "c": "is visiting", "d": "will visit"}, "ans": "a"},
        {"q": "What does 'ethnography' refer to in research methods?", "opts": {"a": "The scientific description of the customs of individual peoples and cultures through immersive fieldwork", "b": "The chemical analysis of plastic elements", "c": "The list of characters in a narrative fable", "d": "The sorting of database primary keys"}, "ans": "a"},
        {"q": "Which preposition fits: 'He is responsible _____ analyzing the survey data.'?", "opts": {"a": "for", "b": "to", "c": "with", "d": "of"}, "ans": "a"},
        {"q": "Complete: Have you ever _____ culture shock while traveling?", "opts": {"a": "experienced", "b": "experience", "c": "experiencing", "d": "experiences"}, "ans": "a"},
        {"q": "What is the synonym of 'homesickness'?", "opts": {"a": "nostalgia or longing for home", "b": "allergy", "c": "excitement", "d": "nausea"}, "ans": "a"},
        {"q": "Which of the following sentences contains a prepositional phrase of location?", "opts": {"a": "The fieldwork was conducted in the rural districts.", "b": "The fieldwork was completed yesterday.", "c": "The fieldwork was very difficult.", "d": "Completing the fieldwork took ten days."}, "ans": "a"},
        {"q": "What grammatical error is in: 'We have ran twenty interviews so far.'?", "opts": {"a": "Incorrect past participle form of the verb 'run' ('ran' instead of 'run')", "b": "Use of 'have' with plural subject", "c": "Spelling of 'interviews'", "d": "Punctuation mark at the end"}, "ans": "a"},
        {"q": "Which preposition is correct in: 'The research is based _____ interviews with local leaders.'?", "opts": {"a": "on or upon", "b": "at", "c": "with", "d": "in"}, "ans": "a"},
        {"q": "What is the past participle of the irregular verb 'choose'?", "opts": {"a": "chosen", "b": "chose", "c": "choosed", "d": "choosing"}, "ans": "a"},
        {"q": "In research methods, what is 'quantitative data'?", "opts": {"a": "Information that can be measured and written down with numbers", "b": "Descriptions of cultural habits using words", "c": "A list of fables and moral lessons", "d": "The states of matter in a lab"}, "ans": "a"},
        {"q": "Complete: The tourist was accused _____ violating local traditions.", "opts": {"a": "of", "b": "with", "c": "for", "d": "at"}, "ans": "a"},
        {"q": "Identify the preposition in: 'The researchers traveled across the region.'", "opts": {"a": "across", "b": "traveled", "c": "the", "d": "region"}, "ans": "a"},
        {"q": "What is the past tense of 'strike' in: 'A sudden realization struck him.'?", "opts": {"a": "struck", "b": "striked", "c": "stricken", "d": "striking"}, "ans": "a"},
        {"q": "What does the word 'disorientation' mean?", "opts": {"a": "a state of mental confusion or lack of direction", "b": "the process of printing reports", "c": "the design of a questionnaire", "d": "the path of a tourist bus"}, "ans": "a"},
        {"q": "Which of these is a homophone for the word 'route' (path)?", "opts": {"a": "root (plant part)", "b": "rate", "c": "rot", "d": "write"}, "ans": "a"},
        {"q": "Complete the present perfect: The research team _____ not published their report yet.", "opts": {"a": "has", "b": "have", "c": "is", "d": "does"}, "ans": "a"},
        {"q": "What is the past participle of 'write'?", "opts": {"a": "written", "b": "wrote", "c": "writes", "d": "writing"}, "ans": "a"},
        {"q": "Identify the preposition of direction in: 'The travelers walked towards the village.'", "opts": {"a": "towards", "b": "walked", "c": "the", "d": "village"}, "ans": "a"},
        {"q": "What is the synonym of the word 'methodology'?", "opts": {"a": "system of methods used in a particular area of study", "b": "list of questions", "c": "feeling of culture shock", "d": "attic of a colossal house"}, "ans": "a"},
        {"q": "Complete: She has worked as a researcher _____ she graduated from university.", "opts": {"a": "since", "b": "for", "c": "during", "d": "until"}, "ans": "a"},
        {"q": "What is the past participle of 'know'?", "opts": {"a": "known", "b": "knew", "c": "knowed", "d": "knowing"}, "ans": "a"},
        {"q": "In research terminology, 'bias' refers to:", "opts": {"a": "a systematic distortion or prejudice in favor of or against one thing", "b": "the length of a report paper", "c": "the spelling of questionnaire options", "d": "the physical location of fieldwork"}, "ans": "a"},
        {"q": "Which preposition is correct in: 'He is familiar _____ the research methods.'?", "opts": {"a": "with", "b": "to", "c": "at", "d": "on"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Which of the following sentences correctly utilizes the present perfect continuous tense to show an ongoing fieldwork activity?", "opts": {"a": "The research team has been conducting interviews in the village since Monday.", "b": "The research team was conducting interviews in the village since Monday.", "c": "The research team had been conducting interviews in the village since Monday.", "d": "The research team conducts interviews in the village since Monday."}, "ans": "a"},
        {"q": "In research methodology, how does 'qualitative research' differ fundamentally from 'quantitative research'?", "opts": {"a": "Qualitative research focuses on understanding human experiences and meanings using words, while quantitative research analyzes numerical data", "b": "Qualitative research is only done in labs, quantitative in the field", "c": "Quantitative research has no questionnaire, qualitative does", "d": "There is no difference in their academic purposes"}, "ans": "a"},
        {"q": "Analyze the syntax: 'It is essential that the questionnaire design be tested before deployment.' What subjunctive construction is demonstrated?", "opts": {"a": "Mandative subjunctive (be-subjunctive)", "b": "Past subjunctive of condition", "c": "Infinitive clause of goal", "d": "Gerund phrase"}, "ans": "a"},
        {"q": "Which sentence contains a prepositional phrase showing a relationship of 'concession'?", "opts": {"a": "Despite the severe culture shock, she successfully completed her research.", "b": "Because of the severe culture shock, she successfully completed her research.", "c": "With the severe culture shock, she successfully completed her research.", "d": "In the middle of the culture shock, she successfully completed her research."}, "ans": "a"},
        {"q": "What does the 'honeymoon stage' represent in the psychological stages of culture shock?", "opts": {"a": "The initial period when the traveler feels excited and fascinated by the new culture", "b": "The phase when the traveler feels angry and homesick", "c": "The final integration into the local society", "d": "The travel booking process"}, "ans": "a"},
        {"q": "Which of the following is a compound preposition?", "opts": {"a": "in front of or in spite of", "b": "through", "c": "between", "d": "against"}, "ans": "a"},
        {"q": "What does 'empirical evidence' mean in fieldwork reports?", "opts": {"a": "information acquired by observation or experimentation directly from the field", "b": "the theoretical background of the author", "c": "the formatting of the report chapters", "d": "the chemical analysis of compounds"}, "ans": "a"},
        {"q": "Complete the sentence: If she _____ the local culture before traveling, she would not have experienced such severe culture shock.", "opts": {"a": "had researched", "b": "researched", "c": "would research", "d": "has researched"}, "ans": "a"},
        {"q": "Identify the preposition in the phrase: 'He succeeded by dint of hard work during the fieldwork.'", "opts": {"a": "by dint of (compound preposition meaning by means of)", "b": "hard", "c": "work", "d": "succeeded"}, "ans": "a"},
        {"q": "What is the past participle form of the irregular verb 'shrink' in fieldwork contexts?", "opts": {"a": "shrunk or shrunken", "b": "shrank", "c": "shrinked", "d": "shrinking"}, "ans": "a"},
        {"q": "In survey design, the term 'random sampling' refers to:", "opts": {"a": "a method where each member of the population has an equal chance of selection", "b": "picking respondents who are nearby and easy to reach", "c": "writing questions in a random order on the page", "d": "exchanging questionnaires with other researchers"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'complement' (to complete)?", "opts": {"a": "compliment (to praise)", "b": "complaint", "c": "complicate", "d": "compliance"}, "ans": "a"},
        {"q": "What is the past participle of 'spin'?", "opts": {"a": "spun", "b": "spinned", "c": "span", "d": "spinning"}, "ans": "a"},
        {"q": "Which sentence contains a correctly punctuated prepositional phrase at the start?", "opts": {"a": "According to the latest survey results, the local community supports the project.", "b": "According to the latest survey results the local community supports the project.", "c": "According, to the latest survey results, the local community supports the project.", "d": "According to the latest survey results, the local community, supports the project."}, "ans": "a"},
        {"q": "What is the term for a preliminary study conducted on a small scale to test the research design before the main fieldwork?", "opts": {"a": "Pilot study", "b": "Ethnography", "c": "Survey analysis", "d": "Document review"}, "ans": "a"},
        {"q": "Which word is a synonym for 'alienation' in the context of culture shock?", "opts": {"a": "estrangement or isolation", "b": "integration", "c": "harmony", "d": "hospitality"}, "ans": "a"},
        {"q": "What is the past participle of the irregular verb 'weep'?", "opts": {"a": "wept", "b": "weeped", "c": "weeping", "d": "weeps"}, "ans": "a"},
        {"q": "In the sentence: 'The scholar traveled to Zeila for the purpose of studying ruins', what is 'for the purpose of' indicating?", "opts": {"a": "Prepositional phrase of intention or goal", "b": "A conditional clause", "c": "A passive voice marker", "d": "A relative clause"}, "ans": "a"},
        {"q": "Which of the following is a key feature of a 'well-designed questionnaire'?", "opts": {"a": "Clear instruction, unambiguous questions, logical layout, and appropriate scale of responses", "b": "Vibrant background colors and large bold fonts", "c": "A list of fables and moral stories", "d": "A chemistry experiment template"}, "ans": "a"},
        {"q": "Complete the proverb: Travel broadens the _____.", "opts": {"a": "mind", "b": "path", "c": "body", "d": "book"}, "ans": "a"},
        {"q": "What is the past participle of 'cling'?", "opts": {"a": "clung", "b": "clinged", "c": "clang", "d": "clings"}, "ans": "a"},
        {"q": "Identify the preposition that indicates agent or means in: 'The questionnaire was analyzed by a professional statistician.'", "opts": {"a": "by", "b": "was", "c": "analyzed", "d": "professional"}, "ans": "a"},
        {"q": "What is the synonym of the word 'adaptation'?", "opts": {"a": "adjustment or integration", "b": "shock", "c": "isolation", "d": "traveling"}, "ans": "a"},
        {"q": "Complete: No sooner had the researcher arrived in the country _____ she had to adjust to the new customs.", "opts": {"a": "than", "b": "then", "c": "when", "d": "before"}, "ans": "a"},
        {"q": "What is the past participle of 'rise'?", "opts": {"a": "risen", "b": "rose", "c": "rised", "d": "rising"}, "ans": "a"},
        {"q": "In anthropological terminology, the term 'participant observation' refers to:", "opts": {"a": "a research method where the researcher lives with the group under study and participates in their activities", "b": "observing the respondents from a far distance using cameras", "c": "asking respondents to design questionnaires", "d": "printing research reports in local papers"}, "ans": "a"},
        {"q": "Which preposition of time refers to 'during a period of time'?", "opts": {"a": "throughout", "b": "hitherto", "c": "at", "d": "formerly"}, "ans": "a"},
        {"q": "What is the past participle of 'stride'?", "opts": {"a": "stridden", "b": "strode", "c": "strided", "d": "striding"}, "ans": "a"},
        {"q": "Identify the suffix that can be added to the adjective 'shocked' to make it a noun.", "opts": {"a": "-ness (shockedness is rare; prefer shock)", "b": "-ment", "c": "-ability", "d": "-ship"}, "ans": "a"},
        {"q": "What grammatical structure is used in: 'Had they prepared the questionnaires, they would have finished the survey.'?", "opts": {"a": "Inverted conditional clause (third conditional)", "b": "Gerund phrase", "c": "Past continuous passive", "d": "Noun clause"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch8_questions():
    # Chapter 8: Unit 15 & 16 (Negotiation Skills & Our Life Today)
    # Focus: Business terms, Negotiation, Agreement, Modern lifestyle, Technology, Comparatives, Superlatives.
    easy = [
        {"q": "What is 'negotiation'?", "opts": {"a": "A discussion aimed at reaching an agreement", "b": "A public presentation in a school", "c": "A chemical reaction in a laboratory", "d": "A poem recitation"}, "ans": "a"},
        {"q": "What is the primary driver of change in 'Our Life Today' compared to the past?", "opts": {"a": "Modern technology and the internet", "b": "Traditional fables and storytelling", "c": "The excavation of ancient ruins", "d": "The study of chemistry compounds"}, "ans": "a"},
        {"q": "Which adjective is a comparative adjective?", "opts": {"a": "faster", "b": "fast", "c": "fastest", "d": "fastly"}, "ans": "a"},
        {"q": "In a negotiation, when both sides give up something to reach an agreement, it is called a:", "opts": {"a": "compromise", "b": "disagreement", "c": "demand", "d": "monologue"}, "ans": "a"},
        {"q": "Which of these is a modern communication device?", "opts": {"a": "Smartphone", "b": "Typewriter", "c": "Camel-halter", "d": "Veranda"}, "ans": "a"},
        {"q": "Complete the comparison: A laptop is _____ than a desktop computer.", "opts": {"a": "more portable", "b": "portable", "c": "most portable", "d": "portabler"}, "ans": "a"},
        {"q": "What do we call a proposal made by one party during a negotiation?", "opts": {"a": "Offer", "b": "Agreement", "c": "Compromise", "d": "Result"}, "ans": "a"},
        {"q": "Complete: Today, people can communicate _____ across the globe.", "opts": {"a": "instantly", "b": "slowly", "c": "yesterday", "d": "pointlessly"}, "ans": "a"},
        {"q": "Which adjective is a superlative adjective?", "opts": {"a": "most advanced", "b": "advanced", "c": "more advanced", "d": "advancing"}, "ans": "a"},
        {"q": "What is the synonym of the word 'agreement'?", "opts": {"a": "harmony or settlement", "b": "dispute", "c": "conflict", "d": "refusal"}, "ans": "a"},
        {"q": "In modern life, using the internet allows students to access a vast amount of _____.", "opts": {"a": "information", "b": "fossil fuels", "c": "ancient ruins", "d": "baking soda"}, "ans": "a"},
        {"q": "Complete the comparison: This is the _____ technology available.", "opts": {"a": "best", "b": "better", "c": "good", "d": "well"}, "ans": "a"},
        {"q": "What negotiation term refers to the final terms accepted by both parties?", "opts": {"a": "Contract or agreement", "b": "Questionnaire", "c": "Debate rule", "d": "Stanza"}, "ans": "a"},
        {"q": "Identify the comparative form of the adjective 'bad'.", "opts": {"a": "worse", "b": "badder", "c": "worst", "d": "bad"}, "ans": "a"},
        {"q": "Which of these is an online service for sending letters digitally?", "opts": {"a": "Email", "b": "Post office", "c": "Veranda", "d": "Fieldwork"}, "ans": "a"},
        {"q": "What is the past tense of 'negotiate'?", "opts": {"a": "negotiated", "b": "negotiating", "c": "negotiates", "d": "negotiate"}, "ans": "a"},
        {"q": "Complete: The internet is the _____ network of computers in the world.", "opts": {"a": "largest", "b": "larger", "c": "large", "d": "more large"}, "ans": "a"},
        {"q": "What is the synonym of the word 'lifestyle'?", "opts": {"a": "way of living", "b": "type of house", "c": "chemical compound", "d": "poetic device"}, "ans": "a"},
        {"q": "Identify the comparative form of 'heavy' in: 'Laptops are _____ than before.'", "opts": {"a": "lighter", "b": "heavyer", "c": "heavier", "d": "lightest"}, "ans": "c"},
        {"q": "What do we call a discussion where two opposing teams argue about a topic?", "opts": {"a": "Debate", "b": "Presentation", "c": "Interview", "d": "Negotiation"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'buy'?", "opts": {"a": "by or bye", "b": "boy", "c": "bay", "d": "bee"}, "ans": "a"},
        {"q": "Identify the comparative adjective in: 'She is happier today.'", "opts": {"a": "happier", "b": "she", "c": "is", "d": "today"}, "ans": "a"},
        {"q": "What do we call a person who represents a company in a business negotiation?", "opts": {"a": "Negotiator", "b": "Orphan", "c": "Tourist", "d": "Respondent"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "Which grammatical rule is applied when comparing two things using a short adjective (e.g. 'tall')?", "opts": {"a": "Add '-er' to the adjective and follow it with 'than' (taller than)", "b": "Add 'more' before the adjective (more tall than)", "c": "Add '-est' to the adjective (tallest than)", "d": "Keep the adjective in its base form"}, "ans": "a"},
        {"q": "Which of the following sentences correctly utilizes a comparative structure for long adjectives?", "opts": {"a": "Smartphone technology is more expensive than traditional television.", "b": "Smartphone technology is expensiver than traditional television.", "c": "Smartphone technology is most expensive than traditional television.", "d": "Smartphone technology is more expensiver than traditional television."}, "ans": "a"},
        {"q": "What is a 'win-win situation' in negotiation skills?", "opts": {"a": "An outcome where both negotiating parties feel satisfied with the agreement reached", "b": "An outcome where one party wins everything and the other loses", "c": "A situation where the negotiation breaks down with no agreement", "d": "A legal dispute solved in a court of law"}, "ans": "a"},
        {"q": "Which comparative is correct in: 'Online learning is _____ than classroom learning for self-disciplined students.'?", "opts": {"a": "more convenient", "b": "convenienter", "c": "most convenient", "d": "more convenienter"}, "ans": "a"},
        {"q": "Complete: The new software is _____, making our work much easier.", "opts": {"a": "more user-friendly", "b": "user-friendlier", "c": "most user-friendly", "d": "user-friendly"}, "ans": "a"},
        {"q": "What does 'digital divide' refer to in modern societies?", "opts": {"a": "The gap between demographics and regions that have access to modern information and communications technology, and those that don't", "b": "Sorting numerical data in a computer database", "c": "Creating a list of files in a scratch directory", "d": "The math equation solving processes"}, "ans": "a"},
        {"q": "Which superlative fits: 'This smartphone has the _____ battery life of all models tested.'?", "opts": {"a": "longest", "b": "longer", "c": "more long", "d": "most long"}, "ans": "a"},
        {"q": "Complete: If you want to negotiate effectively, you _____ know your target before you start.", "opts": {"a": "must", "b": "might", "c": "would", "d": "shall"}, "ans": "a"},
        {"q": "What is the synonym of the negotiation term 'consensus'?", "opts": {"a": "general agreement", "b": "conflict", "c": "proposal", "d": "rejection"}, "ans": "a"},
        {"q": "Which of the following sentences contains a correct superlative adjective?", "opts": {"a": "This is the most advanced internet network in Somalia.", "b": "This is the advancedest internet network in Somalia.", "c": "This is the more advanced internet network in Somalia.", "d": "This is the most advancedest internet network in Somalia."}, "ans": "a"},
        {"q": "What grammatical error is in: 'He is the most smartest student in the class.'?", "opts": {"a": "Double superlative violation ('most smartest' instead of 'smartest')", "b": "Subject-verb agreement error", "c": "Spelling of 'student'", "d": "Punctuation mark at the end"}, "ans": "a"},
        {"q": "Which comparative is correct in: 'His arguments were _____ than yours during the debate.'?", "opts": {"a": "stronger", "b": "more strong", "c": "strongest", "d": "more stronger"}, "ans": "a"},
        {"q": "What is the past participle of the verb 'deal' in business transactions?", "opts": {"a": "dealt", "b": "dealed", "c": "dealing", "d": "deals"}, "ans": "a"},
        {"q": "In business communication, what is a 'counter-offer'?", "opts": {"a": "An offer made in response to a previous offer during negotiation", "b": "An offer that has expired", "c": "A list of rules for public presentations", "d": "A database query command"}, "ans": "a"},
        {"q": "Complete: The new digital device is _____ than the old model.", "opts": {"a": "far more efficient", "b": "far efficienter", "c": "most efficient", "d": "more efficienter"}, "ans": "a"},
        {"q": "Identify the comparative adjective in: 'This task is easier than the last one.'", "opts": {"a": "easier", "b": "task", "c": "than", "d": "last"}, "ans": "a"},
        {"q": "What is the past tense of 'strike' in: 'They struck a bargain.'?", "opts": {"a": "struck", "b": "striked", "c": "stricken", "d": "striking"}, "ans": "a"},
        {"q": "What does the word 'collaboration' mean?", "opts": {"a": "the action of working with someone to produce or create something", "b": "the process of printing reports", "c": "the design of a presentation", "d": "arguing in a business dispute"}, "ans": "a"},
        {"q": "Which of these is a homophone for the word 'sell'?", "opts": {"a": "cell", "b": "soil", "c": "soul", "d": "seal"}, "ans": "a"},
        {"q": "Complete the comparative sentence: The internet connection is _____ today than it was yesterday.", "opts": {"a": "better", "b": "more good", "c": "best", "d": "well"}, "ans": "a"},
        {"q": "What is the past participle of 'negotiate'?", "opts": {"a": "negotiated", "b": "negotiating", "c": "negotiate", "d": "negotiates"}, "ans": "a"},
        {"q": "Identify the superlative adjective in: 'She bought the cheapest smartphone available.'", "opts": {"a": "cheapest", "b": "bought", "c": "smartphone", "d": "available"}, "ans": "a"},
        {"q": "What is the synonym of the word 'deadlock' in negotiation?", "opts": {"a": "a situation in which no progress can be made; a standstill", "b": "a final contract agreement", "c": "a win-win situation", "d": "a business presentation slide"}, "ans": "a"},
        {"q": "Complete: The modern internet network is _____ faster than it was a decade ago.", "opts": {"a": "much", "b": "more", "c": "most", "d": "many"}, "ans": "a"},
        {"q": "What is the past participle of 'sell'?", "opts": {"a": "sold", "b": "selled", "c": "selling", "d": "sells"}, "ans": "a"},
        {"q": "In negotiation terminology, 'BATNA' stands for:", "opts": {"a": "Best Alternative to a Negotiated Agreement", "b": "Business Agreement and Technical Network Association", "c": "Best Analysis of Traditional Narrative Art", "d": "Baking soda and Technical Chemical Association"}, "ans": "a"},
        {"q": "Which comparative is correct in: 'Traveling today is _____ than it was in the past.'?", "opts": {"a": "much safer", "b": "much more safe", "c": "much safest", "d": "saferer"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Which of the following sentences correctly utilizes the double comparative structure to show correlation?", "opts": {"a": "The more prepared you are for the negotiation, the better the final contract will be.", "b": "The most prepared you are for the negotiation, the best the final contract will be.", "c": "The more prepared you are for the negotiation, the more better the final contract will be.", "d": "If you are more prepared for the negotiation, the final contract is better."}, "ans": "a"},
        {"q": "In business communication, how does a 'distributive negotiation' strategy differ from an 'integrative negotiation' strategy?", "opts": {"a": "Distributive focuses on dividing a fixed pie (win-lose), while integrative focuses on expanding the pie (win-win) through collaboration", "b": "Distributive is written, integrative is purely verbal", "c": "Integrative is done in courts, distributive is done in markets", "d": "There is no strategic difference between them"}, "ans": "a"},
        {"q": "Analyze the syntax: 'It is vital that negotiators keep their demands realistic during the initial phase.' What subjunctive construction is demonstrated?", "opts": {"a": "Mandative subjunctive (subjunctive of demand)", "b": "Past subjunctive of condition", "c": "Infinitive clause of purpose", "d": "Gerund phrase"}, "ans": "a"},
        {"q": "Which sentence contains a comparative structure expressing 'gradual increase'?", "opts": {"a": "Our dependence on modern technology is growing stronger and stronger.", "b": "Our dependence on modern technology is growing more strong.", "c": "Our dependence on modern technology is growing the strongest.", "d": "Our dependence on modern technology is growing stronger than ever."}, "ans": "a"},
        {"q": "What does the term 'compromise' connote in high-stakes diplomatic negotiations?", "opts": {"a": "Mutual concession where both sides sacrifice some interests to achieve a greater common goal", "b": "Weakness, surrender, and absolute defeat", "c": "A breakdown of talks with no agreement", "d": "The sorting of database structures"}, "ans": "a"},
        {"q": "Which of the following is an irregular comparative adjective?", "opts": {"a": "further or worse", "b": "spaciouser", "c": "cleverer", "d": "collosal"}, "ans": "a"},
        {"q": "What does 'information overload' mean in modern technology contexts?", "opts": {"a": "the state of having too much information to make a decision or remain focused", "b": "increasing the storage space of a hard drive", "c": "the speed of direct internet connections", "d": "the syntax errors in python codes"}, "ans": "a"},
        {"q": "Complete the sentence: If they _____ their demands, the negotiation would not have ended in a deadlock.", "opts": {"a": "had lowered", "b": "lowered", "c": "would lower", "d": "has lowered"}, "ans": "a"},
        {"q": "Identify the comparative adverb in: 'The business team negotiated more aggressively than their competitors.'", "opts": {"a": "more aggressively", "b": "business", "c": "negotiated", "d": "competitors"}, "ans": "a"},
        {"q": "What is the past participle form of the irregular verb 'slink' in a negotiation context?", "opts": {"a": "slunk", "b": "slinked", "c": "slank", "d": "slinking"}, "ans": "a"},
        {"q": "In business psychology, the term 'anchoring bias' refers to:", "opts": {"a": "the tendency to rely heavily on the first offer or piece of information offered in a negotiation", "b": "focusing only on the negative outcomes of a contract", "c": "changing the subject of the discussion randomly", "d": "printing the agreement in small font sizes"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'sell' (provide goods for money)?", "opts": {"a": "cell (biological unit or phone)", "b": "soul", "c": "seal", "d": "sail"}, "ans": "a"},
        {"q": "What is the past participle of 'strike'?", "opts": {"a": "struck or stricken", "b": "striked", "c": "span", "d": "spinning"}, "ans": "a"},
        {"q": "Which sentence contains a correctly punctuated comparative clause?", "opts": {"a": "Modern lifestyles are far more stressful than they were in the past.", "b": "Modern lifestyles are far more stressful, than they were in the past.", "c": "Modern lifestyles, are far more stressful than they were in the past.", "d": "Modern lifestyles are far, more stressful than they were in the past."}, "ans": "a"},
        {"q": "What is the term for a neutral third party who assists negotiating partners in resolving a dispute with an agreement?", "opts": {"a": "Mediator or arbitrator", "b": "Negotiator", "c": "Respondent", "d": "Stepmother"}, "ans": "a"},
        {"q": "Which word is a synonym for 'concession' in negotiation?", "opts": {"a": "grant or compromise yield", "b": "demand", "c": "deadlock", "d": "contract"}, "ans": "a"},
        {"q": "What is the past participle of the irregular verb 'weep'?", "opts": {"a": "wept", "b": "weeped", "c": "weeping", "d": "weeps"}, "ans": "a"},
        {"q": "In the sentence: 'The team made concessions with a view to securing a final contract', what is 'with a view to' indicating?", "opts": {"a": "Prepositional phrase showing intention or goal", "b": "A conditional clause", "c": "A passive voice marker", "d": "A relative clause"}, "ans": "a"},
        {"q": "Which of the following is a key feature of 'effective integrative negotiation'?", "opts": {"a": "Active listening, empathy, identifying underlying interests, and brainstorming creative solutions", "b": "Making extreme demands, using threats, and refusing to compromise", "c": "Reading from a slide word-for-word", "d": "A chemistry experiment template"}, "ans": "a"},
        {"q": "Complete the proverb: A chain is only as strong as its _____ link.", "opts": {"a": "weakest", "b": "strongest", "c": "middle", "d": "first"}, "ans": "a"},
        {"q": "What is the past participle of 'cling'?", "opts": {"a": "clung", "b": "clinged", "c": "clang", "d": "clings"}, "ans": "a"},
        {"q": "Identify the comparative adjective that modifies a noun in: 'They requested a more flexible schedule.'", "opts": {"a": "more flexible", "b": "requested", "c": "schedule", "d": "schedule is more"}, "ans": "a"},
        {"q": "What is the synonym of the word 'compromise'?", "opts": {"a": "mutual concession or settlement", "b": "deadlock", "c": "demand", "d": "dispute"}, "ans": "a"},
        {"q": "Complete: No sooner had the negotiation started _____ the parties reached a major disagreement.", "opts": {"a": "than", "b": "then", "c": "when", "d": "before"}, "ans": "a"},
        {"q": "What is the past participle of 'rise'?", "opts": {"a": "risen", "b": "rose", "c": "rised", "d": "rising"}, "ans": "a"},
        {"q": "In sociological terminology, the term 'globalization' refers to:", "opts": {"a": "the process by which businesses or other organizations develop international influence or start operating on an international scale", "b": "the process of sorting garbage in local landfills", "c": "asking respondents to design questionnaires", "d": "printing research reports in local papers"}, "ans": "a"},
        {"q": "Which superlative adjective of quantity refers to 'the smallest amount'?", "opts": {"a": "least", "b": "less", "c": "little", "d": "minimumest"}, "ans": "a"},
        {"q": "What is the past participle of 'stride'?", "opts": {"a": "stridden", "b": "strode", "c": "strided", "d": "striding"}, "ans": "a"},
        {"q": "Identify the suffix that can be added to the verb 'negotiate' to make it a noun indicating a person.", "opts": {"a": "-or (negotiator)", "b": "-ment", "c": "-ation", "d": "-ness"}, "ans": "a"},
        {"q": "What grammatical structure is used in: 'Had they negotiated in good faith, they would have signed the contract.'?", "opts": {"a": "Inverted conditional clause (third conditional)", "b": "Gerund phrase", "c": "Past continuous passive", "d": "Noun clause"}, "ans": "a"}
    ]
    return easy, medium, hard

def create_ch9_questions():
    # Chapter 9: Unit 17 & 18 (Problems Caused By Modern Packaging & Allergies)
    # Focus: Packaging, Trash, Waste Disposal, Health, Allergy symptoms, Immune system, Relative clauses, Passive Voice.
    easy = [
        {"q": "What is a main problem caused by modern packaging in cities?", "opts": {"a": "Large amounts of non-biodegradable waste and garbage littering streets", "b": "Lack of school textbooks in classrooms", "c": "Too many poetry guides in libraries", "d": "A chemical reaction in a lab"}, "ans": "a"},
        {"q": "What is an 'allergy'?", "opts": {"a": "A damaging immune response by the body to a substance to which it has become hypersensitive", "b": "A style of building colossal houses", "c": "A business negotiation meeting", "d": "A traditional oral narrative"}, "ans": "a"},
        {"q": "Which sentence is written in the passive voice?", "opts": {"a": "The garbage was collected by the municipal truck.", "b": "The municipal truck collected the garbage.", "c": "The municipal truck collects garbage daily.", "d": "The municipal truck is collecting garbage now."}, "ans": "a"},
        {"q": "In grammar, a clause introduced by a relative pronoun like 'who' or 'which' is a:", "opts": {"a": "relative clause", "b": "conditional clause", "c": "subordinate conjunction", "d": "prepositional phrase"}, "ans": "a"},
        {"q": "Which of these is a common allergen?", "opts": {"a": "Pollen or peanuts", "b": "Baking soda", "c": "Plastic bags", "d": "Modern computer screen"}, "ans": "a"},
        {"q": "Complete the passive sentence: The box _____ wrapped in plastic last night.", "opts": {"a": "was", "b": "is", "c": "were", "d": "been"}, "ans": "a"},
        {"q": "What do we call a place where garbage is buried under soil layers?", "opts": {"a": "Landfill", "b": "Veranda", "c": "Ecosystem", "d": "Ruins"}, "ans": "a"},
        {"q": "Complete: The doctor, _____ treated my allergy, is very professional.", "opts": {"a": "who", "b": "which", "c": "whom", "d": "whose"}, "ans": "a"},
        {"q": "What system in the body protects us from diseases but reacts during allergies?", "opts": {"a": "Immune system", "b": "Nervous system", "c": "Digestive system", "d": "Respiratory system"}, "ans": "a"},
        {"q": "What is the synonym of the word 'symptom'?", "opts": {"a": "sign or indication of illness", "b": "treatment", "c": "cause", "d": "medicine"}, "ans": "a"},
        {"q": "In Unit 17, modern packaging materials are made mostly of _____.", "opts": {"a": "plastics and cardboard", "b": "wood and leaves", "c": "iron and steel", "d": "chemical liquids"}, "ans": "a"},
        {"q": "Which relative pronoun is used for things in a relative clause?", "opts": {"a": "which", "b": "who", "c": "whom", "d": "whose"}, "ans": "a"},
        {"q": "Complete: These pills _____ prescribed by the doctor yesterday.", "opts": {"a": "were", "b": "was", "c": "are", "d": "been"}, "ans": "a"},
        {"q": "What symptom is common when pollen enters an allergic person's nose?", "opts": {"a": "Sneezing and runny nose", "b": "Stomach blockage", "c": "Roaring sound in ears", "d": "Extreme wealth status"}, "ans": "a"},
        {"q": "Which relative pronoun shows possession in: 'The boy _____ mother is a doctor is my friend.'?", "opts": {"a": "whose", "b": "who", "c": "whom", "d": "which"}, "ans": "a"},
        {"q": "What is the past tense of the verb 'wrap'?", "opts": {"a": "wrapped", "b": "wrapping", "c": "wraps", "d": "wrap"}, "ans": "a"},
        {"q": "Complete: The packaging waste _____ thrown into the landfill daily.", "opts": {"a": "is", "b": "are", "c": "were", "d": "been"}, "ans": "a"},
        {"q": "What is a synonym of the word 'immune'?", "opts": {"a": "resistant or protected", "b": "weak", "c": "allergic", "d": "sensitive"}, "ans": "a"},
        {"q": "Identify the relative pronoun in: 'The package which arrived today was damaged.'", "opts": {"a": "which", "b": "package", "c": "arrived", "d": "damaged"}, "ans": "a"},
        {"q": "What does a dermatologist specialize in treating?", "opts": {"a": "Skin conditions and skin allergies", "b": "Heart diseases", "c": "Database programming", "d": "Poetry stanzas"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'waste'?", "opts": {"a": "waist", "b": "west", "c": "wet", "d": "worst"}, "ans": "a"},
        {"q": "Identify the relative clause in: 'I visited the clinic that is near the school.'", "opts": {"a": "that is near the school", "b": "I visited the clinic", "c": "visited the clinic", "d": "near the school"}, "ans": "a"},
        {"q": "What is a medical term for a severe, life-threatening allergic reaction?", "opts": {"a": "Anaphylaxis", "b": "Symptom", "c": "Immunity", "d": "Therapy"}, "ans": "a"}
    ]
    
    medium = [
        {"q": "When changing a sentence from active voice to passive voice, what happens to the active object?", "opts": {"a": "It becomes the grammatical subject of the passive sentence", "b": "It remains the object at the end of the sentence", "c": "It is completely deleted from the sentence", "d": "It changes into a relative pronoun"}, "ans": "a"},
        {"q": "Which of the following represents the correct passive voice for: 'The researcher analyzed the survey data.'?", "opts": {"a": "The survey data was analyzed by the researcher.", "b": "The survey data is analyzed by the researcher.", "c": "The survey data had analyzed by the researcher.", "d": "The researcher was analyzed by the survey data."}, "ans": "a"},
        {"q": "What is the primary role of the 'immune system' in human health?", "opts": {"a": "To detect and neutralize foreign substances, pathogens, and viruses in the body", "b": "To pump blood to the organs", "c": "To digest food and absorb nutrients", "d": "To regulate body temperature"}, "ans": "a"},
        {"q": "Which relative pronoun is correct in: 'The landfill, _____ is located near the village, has reached its capacity.'?", "opts": {"a": "which", "b": "who", "c": "whom", "d": "whose"}, "ans": "a"},
        {"q": "Complete: The allergy symptoms, which _____ by pollen, resolved after taking antihistamines.", "opts": {"a": "were caused", "b": "caused", "c": "are caused", "d": "will cause"}, "ans": "a"},
        {"q": "What does 'non-biodegradable packaging' refer to in modern waste management?", "opts": {"a": "Wrapping materials like Styrofoam and plastic that cannot be decomposed by natural organisms", "b": "Organic banana leaves used to wrap food", "c": "Cardboard boxes that dissolve in water", "d": "Reusing bottles for drinking water"}, "ans": "a"},
        {"q": "Which passive construction is correct in: 'The garbage _____ collected every Friday morning.'?", "opts": {"a": "is", "b": "are", "c": "were", "d": "been"}, "ans": "a"},
        {"q": "Complete: The doctor _____ treats my asthma has also diagnosed my skin allergy.", "opts": {"a": "who", "b": "which", "c": "whom", "d": "whose"}, "ans": "a"},
        {"q": "What is the synonym of the word 'hypersensitive'?", "opts": {"a": "abnormally sensitive", "b": "immune", "c": "strong", "d": "healthy"}, "ans": "a"},
        {"q": "Which of the following sentences contains a non-defining relative clause?", "opts": {"a": "Modern packaging, which is made of plastic, is difficult to recycle.", "b": "Modern packaging which is made of plastic is difficult to recycle.", "c": "Modern packaging is a material which is difficult to recycle.", "d": "Being made of plastic, modern packaging is difficult to recycle."}, "ans": "a"},
        {"q": "What grammatical error is in: 'The packaging materials was dumped in the ocean.'?", "opts": {"a": "Subject-verb agreement error ('was' instead of plural 'were')", "b": "Use of passive voice", "c": "Spelling of 'materials'", "d": "Punctuation mark at the end"}, "ans": "a"},
        {"q": "Which relative pronoun is correct in: 'The child _____ skin was red had an allergic reaction.'?", "opts": {"a": "whose", "b": "who", "c": "whom", "d": "which"}, "ans": "a"},
        {"q": "What is the past participle of the irregular verb 'throw' when talking about garbage?", "opts": {"a": "thrown", "b": "threw", "c": "throwed", "d": "throwing"}, "ans": "a"},
        {"q": "In medical science, what is an 'antihistamine'?", "opts": {"a": "A drug that inhibits the physiological effects of histamine, used in treating allergies", "b": "A vaccine against viral infections", "c": "A type of chemical compound used in packaging", "d": "A symptom of severe asthma"}, "ans": "a"},
        {"q": "Complete: The patient was advised _____ avoid eating peanuts due to his severe allergy.", "opts": {"a": "to", "b": "with", "c": "for", "d": "at"}, "ans": "a"},
        {"q": "Identify the relative pronoun in: 'The doctor whom we met yesterday is an allergist.'", "opts": {"a": "whom", "b": "doctor", "c": "met", "d": "allergist"}, "ans": "a"},
        {"q": "What is the past tense of 'strike' in: 'She was struck by an allergic reaction.'?", "opts": {"a": "struck", "b": "striked", "c": "stricken", "d": "striking"}, "ans": "a"},
        {"q": "What does the word 'disposal' mean?", "opts": {"a": "the action or process of getting rid of something", "b": "the process of printing packaging boxes", "c": "the design of a clinical test", "d": "the path of a garbage truck"}, "ans": "a"},
        {"q": "Which of these is a homophone for the word 'heal' (cure)?", "opts": {"a": "heel (foot part) or he'll (he will)", "b": "hill", "c": "hale", "d": "hall"}, "ans": "a"},
        {"q": "Complete the passive sentence: The patient _____ taken to the referral hospital immediately.", "opts": {"a": "was", "b": "is", "c": "were", "d": "been"}, "ans": "a"},
        {"q": "What is the past participle of 'write' in: 'The medical report was written by the doctor.'?", "opts": {"a": "written", "b": "wrote", "c": "writes", "d": "writing"}, "ans": "a"},
        {"q": "Identify the relative pronoun showing objective case in: 'The doctor whom you recommended is excellent.'", "opts": {"a": "whom", "b": "doctor", "c": "recommended", "d": "excellent"}, "ans": "a"},
        {"q": "What is the synonym of the word 'severity'?", "opts": {"a": "seriousness or gravity", "b": "mildness", "c": "speed", "d": "duration"}, "ans": "a"},
        {"q": "Complete: She has been allergic to milk _____ she was an infant.", "opts": {"a": "since", "b": "for", "c": "during", "d": "until"}, "ans": "a"},
        {"q": "What is the past participle of 'know' in: 'He is known to have a peanut allergy.'?", "opts": {"a": "known", "b": "knew", "c": "knowed", "d": "knowing"}, "ans": "a"},
        {"q": "In medical terminology, 'immunization' refers to:", "opts": {"a": "the action of making a person immune to an infectious disease, typically by vaccination", "b": "the process of getting an allergic reaction", "c": "the sorting of medical garbage in a landfill", "d": "the treatment of skin rashes"}, "ans": "a"},
        {"q": "Which relative pronoun is correct in: 'The packaging _____ was imported is recyclable.'?", "opts": {"a": "that or which", "b": "who", "c": "whom", "d": "whose"}, "ans": "a"}
    ]
    
    hard = [
        {"q": "Which of the following sentences correctly utilizes the passive voice in the present perfect tense?", "opts": {"a": "Millions of plastic containers have been discarded in our municipal landfill this year.", "b": "Millions of plastic containers were discarded in our municipal landfill this year.", "c": "Millions of plastic containers have discarded in our municipal landfill this year.", "d": "Millions of plastic containers are discarded in our municipal landfill this year."}, "ans": "a"},
        {"q": "In immunology, how does a 'food allergy' differ fundamentally from a 'food intolerance'?", "opts": {"a": "A food allergy involves an immune system response (IgE antibodies), whereas intolerance does not involve the immune system", "b": "Food intolerance is always fatal, allergy is not", "c": "Food allergy only occurs in adults, intolerance in children", "d": "There is no physiological difference between them"}, "ans": "a"},
        {"q": "Analyze the syntax: 'The doctor recommended that the patient be tested for peanut allergies immediately.' What subjunctive construction is demonstrated?", "opts": {"a": "Mandative subjunctive (be-subjunctive)", "b": "Past subjunctive of condition", "c": "Infinitive clause of goal", "d": "Gerund phrase"}, "ans": "a"},
        {"q": "Which sentence contains a non-defining relative clause modifying a medical condition?", "opts": {"a": "Anaphylaxis, which is a severe systemic allergic reaction, requires an immediate epinephrine injection.", "b": "Anaphylaxis which is a severe systemic allergic reaction requires an immediate epinephrine injection.", "c": "Anaphylaxis is a severe systemic allergic reaction which requires an epinephrine injection.", "d": "Being a severe systemic allergic reaction, anaphylaxis requires an epinephrine injection."}, "ans": "a"},
        {"q": "What does the term 'biodegradable polymer' represent in modern green packaging research?", "opts": {"a": "A plastic material that can be broken down by microorganisms into water, carbon dioxide, and biomass", "b": "A packaging box made of strong steel frames", "c": "A liquid chemical solution that freezes at room temperature", "d": "The sorting of medical waste in hospitals"}, "ans": "a"},
        {"q": "Which of the following is a relative adverb of reason in: 'The reason why she avoids peanuts is her severe allergy.'?", "opts": {"a": "why", "b": "reason", "c": "avoids", "d": "allergy"}, "ans": "a"},
        {"q": "What does 'hives' (urticaria) mean in allergy diagnostics?", "opts": {"a": "red, itchy, raised welts on the skin caused by an allergic reaction", "b": "coughing and wheezing sounds in the lungs", "c": "a stomach ache after eating solid food", "d": "the structures built by bees in a forest"}, "ans": "a"},
        {"q": "Complete the sentence: If the patient _____ the epinephrine shot immediately, he would have suffered fatal anaphylaxis.", "opts": {"a": "had not received", "b": "did not receive", "c": "would not receive", "d": "has not received"}, "ans": "a"},
        {"q": "Identify the passive voice with a modal verb in: 'Discarded packaging should be recycled to prevent pollution.'", "opts": {"a": "should be recycled", "b": "discarded packaging", "c": "prevent pollution", "d": "should prevent"}, "ans": "a"},
        {"q": "What is the past participle form of the irregular verb 'swell' in allergy descriptions?", "opts": {"a": "swollen", "b": "swelled", "c": "swelling", "d": "swells"}, "ans": "a"},
        {"q": "In municipal waste management, the term 'source separation' refers to:", "opts": {"a": "the sorting of recyclable materials from garbage at the point of origin (homes, businesses)", "b": "digging deep trenches in the landfill", "c": "printing recycling guidelines on packaging boxes", "d": "exporting garbage to other countries"}, "ans": "a"},
        {"q": "Which of the following is a homophone for the word 'sew' (join with stitches)?", "opts": {"a": "sow (plant seeds) or so (therefore)", "b": "saw", "c": "sue", "d": "sea"}, "ans": "a"},
        {"q": "What is the past participle of 'spin'?", "opts": {"a": "spun", "b": "spinned", "c": "span", "d": "spinning"}, "ans": "a"},
        {"q": "Which sentence contains a correctly punctuated non-defining relative clause?", "opts": {"a": "Baking soda, which is NaHCO3, can be used to treat mild skin rashes.", "b": "Baking soda which is NaHCO3 can be used to treat mild skin rashes.", "c": "Baking soda, which is NaHCO3 can be used to treat mild skin rashes.", "d": "Baking soda which is NaHCO3, can be used to treat mild skin rashes."}, "ans": "a"},
        {"q": "What is the term for a medical test where potential allergens are applied to the skin via scratches to check for reactions?", "opts": {"a": "Skin prick test", "b": "Blood immunization test", "c": "Carbon dating test", "d": "Chemical analysis test"}, "ans": "a"},
        {"q": "Which word is a synonym for 'exacerbate' in the context of allergies?", "opts": {"a": "worsen or aggravate", "b": "alleviate", "c": "cure", "d": "prevent"}, "ans": "a"},
        {"q": "What is the past participle of the irregular verb 'weep'?", "opts": {"a": "wept", "b": "weeped", "c": "weeping", "d": "weeps"}, "ans": "a"},
        {"q": "In the sentence: 'The municipal council banned plastic bags with a view to reducing litter', what is 'with a view to' indicating?", "opts": {"a": "Prepositional phrase of intention or purpose", "b": "A conditional clause", "c": "A passive voice marker", "d": "A relative clause"}, "ans": "a"},
        {"q": "Which of the following is a key symptom of 'severe asthma' during an allergic reaction?", "opts": {"a": "Shortness of breath, wheezing, coughing, and chest tightness", "b": "Red skin rashes without itching", "c": "A severe headache and fever", "d": "Nothing; asthma has no symptoms"}, "ans": "a"},
        {"q": "Complete the proverb: An ounce of prevention is worth a pound of _____.", "opts": {"a": "cure", "b": "medicine", "c": "health", "d": "treatment"}, "ans": "a"},
        {"q": "What is the past participle of 'cling'?", "opts": {"a": "clung", "b": "clinged", "c": "clang", "d": "clings"}, "ans": "a"},
        {"q": "Identify the relative clause that modifies the object in: 'The doctor treated the patient whose skin was swollen.'", "opts": {"a": "whose skin was swollen", "b": "The doctor treated the patient", "c": "treated the patient", "d": "whose skin"}, "ans": "a"},
        {"q": "What is the synonym of the word 'alleviate'?", "opts": {"a": "relieve or lessen", "b": "worsen", "c": "provoke", "d": "diagnose"}, "ans": "a"},
        {"q": "Complete: No sooner had the package been opened _____ the dust triggered her allergy.", "opts": {"a": "than", "b": "then", "c": "when", "d": "before"}, "ans": "a"},
        {"q": "What is the past participle of 'rise'?", "opts": {"a": "risen", "b": "rose", "c": "rised", "d": "rising"}, "ans": "a"},
        {"q": "In environmental physiology, the term 'allergenicity' refers to:", "opts": {"a": "the capacity of a chemical or biological substance to induce an allergic response", "b": "the speed at which plastic degrades in landfills", "c": "the amount of pollen in the forest", "d": "the treatment of asthma"}, "ans": "a"},
        {"q": "Which relative pronoun refers to a location in relative clauses?", "opts": {"a": "where", "b": "when", "c": "why", "d": "which"}, "ans": "a"},
        {"q": "What is the past participle of 'stride'?", "opts": {"a": "stridden", "b": "strode", "c": "strided", "d": "striding"}, "ans": "a"},
        {"q": "Identify the suffix that can be added to the adjective 'allergic' to make it a noun indicating the allergy-inducing substance.", "opts": {"a": "-en (allergen)", "b": "-ness", "c": "-ment", "d": "-ship"}, "ans": "a"},
        {"q": "What grammatical structure is used in: 'Had they recycled the packaging waste, the environment would be cleaner.'?", "opts": {"a": "Inverted conditional clause (third conditional)", "b": "Gerund phrase", "c": "Past continuous passive", "d": "Noun clause"}, "ans": "a"}
    ]
    return easy, medium, hard

def main():
    seed_file_path = 'lib/services/seed_data.dart'
    
    # 1. Read seed_data.dart
    with open(seed_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx_raw = content.find(start_str)
    if start_idx_raw == -1:
        print("Could not find fullSeedJson")
        return
        
    start_idx = content.find('{', start_idx_raw)
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find JSON bounds")
        return
        
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # 2. Add English Subject
    subjects = data.get('subjects', [])
    # Remove existing english to avoid duplicates if rerun
    subjects = [s for s in subjects if s['id'] != 'eng']
    subjects.append({
        'name': 'English',
        'id': 'eng'
    })
    data['subjects'] = subjects
    
    # 3. Add Chapters
    chapters = data.get('chapters', [])
    # Remove existing english chapters
    chapters = [c for c in chapters if c['subjectId'] != 'eng']
    
    new_chapters = [
        {'subjectId': 'eng', 'title': 'Unit 1 & 2: Never Forget & Oral Presentation', 'id': 'eng_ch1'},
        {'subjectId': 'eng', 'title': 'Unit 3 & 4: A Colossal House & Poetry Guide', 'id': 'eng_ch2'},
        {'subjectId': 'eng', 'title': 'Unit 5 & 6: The Lion with a Thorn in His Paw & Oral Literature', 'id': 'eng_ch3'},
        {'subjectId': 'eng', 'title': 'Unit 7 & 8: The Father and his Son & Edible Soda', 'id': 'eng_ch4'},
        {'subjectId': 'eng', 'title': 'Unit 9 & 10: The Motherless Girl & Societies In The Past', 'id': 'eng_ch5'},
        {'subjectId': 'eng', 'title': 'Unit 11 & 12: Nature Conservation & The Killer Plastic', 'id': 'eng_ch6'},
        {'subjectId': 'eng', 'title': 'Unit 13 & 14: Culture Shock & Field Work', 'id': 'eng_ch7'},
        {'subjectId': 'eng', 'title': 'Unit 15 & 16: Negotiation Skills & Our Life Today', 'id': 'eng_ch8'},
        {'subjectId': 'eng', 'title': 'Unit 17 & 18: Problems Caused By Modern Packaging & Allergies', 'id': 'eng_ch9'},
    ]
    
    chapters.extend(new_chapters)
    data['chapters'] = chapters
    
    # 4. Generate Questions for each of the 9 chapters
    all_questions = []
    
    ch_generators = {
        1: create_ch1_questions,
        2: create_ch2_questions,
        3: create_ch3_questions,
        4: create_ch4_questions,
        5: create_ch5_questions,
        6: create_ch6_questions,
        7: create_ch7_questions,
        8: create_ch8_questions,
        9: create_ch9_questions,
    }
    
    for ch_num in range(1, 10):
        easy_b, med_b, hard_b = ch_generators[ch_num]()
        
        # Verify sizes
        if len(easy_b) < 23 or len(med_b) < 27 or len(hard_b) < 30:
            print(f"Error: Chapter {ch_num} has insufficient questions! Easy: {len(easy_b)}, Medium: {len(med_b)}, Hard: {len(hard_b)}")
            return
            
        ch_id = f"eng_ch{ch_num}"
        
        # Take exactly the requested counts
        # Easy: 23
        for i in range(23):
            bq = easy_b[i]
            all_questions.append({
                "id": f"Eng_Ch{ch_num}_Q{str(i+1).zfill(2)}",
                "question": bq["q"],
                "options": bq["opts"],
                "correctAnswer": bq["ans"],
                "difficultyLevel": "easy",
                "subjectId": "eng",
                "chapterId": ch_id
            })
            
        # Medium: 27
        for i in range(27):
            bq = med_b[i]
            all_questions.append({
                "id": f"Eng_Ch{ch_num}_Q{str(i+24).zfill(2)}",
                "question": bq["q"],
                "options": bq["opts"],
                "correctAnswer": bq["ans"],
                "difficultyLevel": "medium",
                "subjectId": "eng",
                "chapterId": ch_id
            })
            
        # Hard: 30
        for i in range(30):
            bq = hard_b[i]
            all_questions.append({
                "id": f"Eng_Ch{ch_num}_Q{str(i+51).zfill(2)}",
                "question": bq["q"],
                "options": bq["opts"],
                "correctAnswer": bq["ans"],
                "difficultyLevel": "hard",
                "subjectId": "eng",
                "chapterId": ch_id
            })
            
    # 5. Merge new questions
    questions = data.get('questions', [])
    # Remove existing english questions
    questions = [q for q in questions if q.get('subjectId') != 'eng']
    questions.extend(all_questions)
    data['questions'] = questions
    
    # 6. Write back to seed_data.dart
    updated_json = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content[:start_idx] + updated_json + "\n" + content[end_idx:]
    
    with open(seed_file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully generated {len(all_questions)} questions for English subject (9 chapters) and merged them into seed_data.dart!")

if __name__ == '__main__':
    main()
