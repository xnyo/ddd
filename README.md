## ddd
### Track Datadog updates through Discord

## Requirements
- Python 3.5
- bottle
- gevent
- requests

## Setting up
- Clone the repository
- Install the required dependencies with
```
$ pip install -r requirements.txt
````
- Go on your Discord server and add a webhook for each channel you'd like to post Datadog updates to.  
- Then edit `settings.json` and add a new key to the `alternative_hooks` dictionary for each channel. That key must contains the Discord webhook URL for that channel, **ending with `/slack`** (eg: if your discord webhook url is `https://discordapp.com/api/webhooks/xxxxxxx`, you have to put `https://discordapp.com/api/webhooks/xxxxxxx/slack`).  
- Don't forget to configure `default_hook` too. All the requests that should go to a channel that's not listed to a config file will be posted to the `default_hook`.  
- Launch `ddd.py`. This will start a bottle webserver will start on port **44132**. You can change the port using the `--port` CLI argument. Once the server is started, it'll redirect all the incoming requests that match the Slack webhook structure to a Discord webhook.  
- To complete the set up, log in to Datadog, go in the **Integrations** page, add a **Slack** integration and set **Slack Service Hook** to your ddd address (eg: http://1.2.3.4:44132/).  
- Then, still in the Slack integration set up page, add as many channels as you want.  

## License
MIT