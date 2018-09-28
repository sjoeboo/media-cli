from plexapi.myplex import MyPlexAccount
import logging

logger = logging.getLogger('media-cli')

def get_server(plex_creds):
    logger.info("Logging into Plex...")
    account = MyPlexAccount(plex_creds['email'], plex_creds['password'])
    logger.info("Connecting to server {}".format(plex_creds['server']))
    plex = account.resource(plex_creds['server']).connect()
    return plex

def sync(plex_creds):
    server=get_server(plex_creds)
    logger.info("Triggered Plex Library Update")
    server.library.update()
