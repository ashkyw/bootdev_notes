def get_players_to_message(lobbies, selected_lobbies, muted_players):
    players_to_message = set()

    for lobby_name in selected_lobbies:
        if lobby_name in lobbies:
            players_to_message = players_to_message.union(lobbies[lobby_name])

    players_to_message = players_to_message.difference(muted_players)
    return players_to_message

(W3)[https://www.w3schools.com/python/python_ref_set.asp]
