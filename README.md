# blaze-autobettor
Enhance your Blaze gaming! This repo features "Blaze Double Bot" and "Telegram B.O.T." scripts. The first automates bets based on JSON cues, while the second syncs color info from Telegram. Elevate your Blaze experience with seamless automation!


<b>Blaze Double Bot</b>

This repository contains an automated betting system for the Blaze website using Python. The system is composed of two distinct scripts: the "Blaze Double Bot" and the "Telegram B.O.T".

<b>Blaze Double Bot:</b>

"Blaze Double Bot" is implemented in Python with the help of Selenium. It constantly monitors a JSON file that stores crucial information for betting. Whenever there is a change in this file, the script reacts, identifying the new color to be played and executing bets automatically.

<b>Telegram B.O.T:</b>

"Telegram B.O.T" works as a complement to the first script. It checks a specific channel on Telegram for new messages that contain information about the color to be played. When a new color is launched on the channel, the script recognizes it, saves this information in the JSON file shared with the "Blaze Double Bot" and thus starts the betting process.

This system provides a flexible and automated approach to the "double" betting method on the Blaze website, making the process more efficient and responsive to changing playing conditions.
