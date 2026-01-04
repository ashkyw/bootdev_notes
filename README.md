# boot_dev_notes

def get_players_to_message(lobbies, selected_lobbies, muted_players):
#    players_to_message = set() remove
#    if selected_lobbies == set():
#        return set()

    for lobby_name in selected_lobbies:
        if lobby_name in lobbies:
            selected_players = set(lobbies[lobby_name])

        players_to_message = selected_players | muted_players
#    players_to_message = players_to_message.intersection(muted_players)
    return players_to_message
