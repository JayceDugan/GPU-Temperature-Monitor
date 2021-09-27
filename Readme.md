# Nicehash GPU Temperature Monitor

This project runs in parallel with `Nicehash QuickMiner` and `Open Hardware Monitor` to monitor the active GPU 
temperature while the miner is running. In the event the temperature exceeds the set safe temperature, the mining 
application is killed and a text is sent to the configured mobile number via `Twilio` informing of the current GPU 
temperature and that application has exited.

Just a small project created to err on the side of safety when learning the world of cryptocurrency and mining.
