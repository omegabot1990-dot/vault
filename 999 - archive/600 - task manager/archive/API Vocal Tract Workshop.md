---
tags:
  - academic
  - api
description: vocal tract workshop for API
due date: 2024-09-27
start date: 2024-09-26
end date: 2024-09-28
status: Archive
importance level: important
urgency level: urgent
task type: execute
story points: 
parent nodes:
  - "[[audio processing and indexing]]"
child nodes: 
recurrent:
---
[Link to Google Docs](https://docs.google.com/document/d/11QBMMwahHo6byNs3RIpk8Lnf0Ncp0mhcBV1u4Ss-LEM/edit?usp=sharing)

![[audio_processing_and_indexing_vocal_tract_workshop.pdf]]


## Task 1

1. Followed the steps outlined in 7.3 of the manual and created a vocal tract.
2. Started with an "o" and played around with the yellow control parameters till I got to a point where I felt I had a robotic voice like Stephen Hawking getting startled and saying "Ahh!".

## Task 2

1. Followed the steps outlined in 7.4 to create 3 vocal tract shapes
	1. vowel - a
	2. vowel - i
	3. vowel - o

## Task 3

1. I selected example 6 in English to edit. 
2. Originally it said: "I think I have a German accent."
3. Plan was to change it into: "You think you have a German accent."
4. First update was with the Vowel Gestures, what was before a sequence "i" and "e", I changed into "e" and "u" 
	1. This step was more or less intuitive 

## Task 4

1. I started with defining the melody and decided to fit the words in after I have a concrete melody
2. I found out that F0 was the controlling variable that essentially formed the pitch of the sound
	1. I decided to go with the Key of C, sticking to the major scale
		1. ~60 st being C (1st)
		2. ~65.5 st being F (4th)
		3. ~67.5 st being G (5th)
		4. ~64 st being E (3rd)
	2. My melody would be 1 - 4 - 5 - 3 - 1, or in other words C - F - G - E - C
	3. First word is "Hi"
		1. Which starts with a consonant /h/
			1. Can be made with a Glottal Shape Gesture
				1. voiceless-fricative
				2. Duration set to 150
		2. Second is a vowel /a/ followed by a vowel /i/
			1. Duration of /a/ has been set to 150
			2. Duration of /i/ has been set to 50
		3. The F0 value is set to 60 for this and the total duration of the first word like all words has been set to 500ms
	4. Second word is "Its"
		1. Which starts with the vowel /I/
			1. Duration set to 200ms
		2. Second is a consonant /t/
			1. Can be made by a combination of,
				1.  Tongue Tip Gesture 
					1. tt-alveolar-closure set to 150ms
					2.  set to 50ms
		3. Third is a consonant /z/
			1.  Tongue Tip Gesture 
				1. tt-alveolar-fricative set to 200ms
			2. Glottal Shape Gesture
				1. voiced-fricative set to 200ms
	5. Third word is "Me"
		1. Which starts with a /m/
			1. Can be made with, 
				1. Lip Gesture
					1. ll-labial-closure set to 200ms
				2. Velic Gesture
					1. Opens to 0.7 set to 200ms
		2. Second is a /i/
			1. Duration is set to 200ms
	6. Fourth word is "You"
		1. Which starts with /j/,
			1. Tongue Body Gesture
				1. tb-palatal-fricative set to 200ms
		2. Second is /u/,
			1. Can be made with a Vowel Gesture
				1. u set to 300ms
			2. And a Lip Gesture
				1. ll-labial-closure overlapping and set to 100ms
	7. Fifth word is "See"
		1. Which starts with a /s/,
			1. Tongue Tip Gesture
				1. tt-alveolar-fricative set to 200ms
		2. Second is /i/
			1. Vowel Gesture
				1. i for 300ms