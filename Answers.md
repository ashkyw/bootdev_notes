    possible_paths = permutations(cities)
    total_distance = 0
    print(f"Paths: {possible_paths}")
    for full_path in possible_paths:
        for path in full_path:
            for i in paths[path]:
                total_distance += i
                if total_distance < dist:
                    return True

    return False
        
