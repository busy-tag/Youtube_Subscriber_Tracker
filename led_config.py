import json

def configure_leds(increased, drive_letter):
    # Path to the configuration file
    config_path = rf"{drive_letter}:\config.json"
    
    # Load the current configuration
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    # Update the configuration based on whether the subscriber count increased or decreased
    if increased:
        config["solid_color"]["color"] = "00FF00"
        config["custom_pattern_arr"] = [
            {"led_bits":129,"color":"00FF00","speed":5,"delay":50},{"led_bits":130,"color":"00FF00","speed":5,"delay":50},
            {"led_bits":132,"color":"00FF00","speed":5,"delay":50},{"led_bits":136,"color":"00FF00","speed":5,"delay":50},
            {"led_bits":144,"color":"00FF00","speed":5,"delay":50},{"led_bits":160,"color":"00FF00","speed":5,"delay":50},
            {"led_bits":192,"color":"00FF00","speed":5,"delay":50},{"led_bits":129,"color":"00FF00","speed":5,"delay":50},
            {"led_bits":130,"color":"00FF00","speed":5,"delay":50},{"led_bits":132,"color":"00FF00","speed":5,"delay":50},
            {"led_bits":136,"color":"00FF00","speed":5,"delay":50},{"led_bits":144,"color":"00FF00","speed":5,"delay":50},
            {"led_bits":160,"color":"00FF00","speed":5,"delay":50},{"led_bits":192,"color":"00FF00","speed":5,"delay":50},
            {"led_bits":129,"color":"00FF00","speed":5,"delay":50},{"led_bits":130,"color":"00FF00","speed":5,"delay":50},
            {"led_bits":132,"color":"00FF00","speed":5,"delay":50},{"led_bits":136,"color":"00FF00","speed":5,"delay":50},
            {"led_bits":144,"color":"00FF00","speed":5,"delay":50},{"led_bits":160,"color":"00FF00","speed":5,"delay":50},
            {"led_bits":192,"color":"00FF00","speed":5,"delay":50},{"led_bits":127,"color":"000000","speed":15,"delay":20},
            {"led_bits":127,"color":"00FF00","speed":20,"delay":30},{"led_bits":127,"color":"000000","speed":20,"delay":30},
            {"led_bits":127,"color":"00FF00","speed":20,"delay":30},{"led_bits":127,"color":"000000","speed":20,"delay":30}
        ]
    else:
        config["solid_color"]["color"] = "FF0000"
        config["custom_pattern_arr"] = [
            {"led_bits":129,"color":"FF0000","speed":5,"delay":50},{"led_bits":130,"color":"FF0000","speed":5,"delay":50},
            {"led_bits":132,"color":"FF0000","speed":5,"delay":50},{"led_bits":136,"color":"FF0000","speed":5,"delay":50},
            {"led_bits":144,"color":"FF0000","speed":5,"delay":50},{"led_bits":160,"color":"FF0000","speed":5,"delay":50},
            {"led_bits":192,"color":"FF0000","speed":5,"delay":50},{"led_bits":129,"color":"FF0000","speed":5,"delay":50},
            {"led_bits":130,"color":"FF0000","speed":5,"delay":50},{"led_bits":132,"color":"FF0000","speed":5,"delay":50},
            {"led_bits":136,"color":"FF0000","speed":5,"delay":50},{"led_bits":144,"color":"FF0000","speed":5,"delay":50},
            {"led_bits":160,"color":"FF0000","speed":5,"delay":50},{"led_bits":192,"color":"FF0000","speed":5,"delay":50},
            {"led_bits":129,"color":"FF0000","speed":5,"delay":50},{"led_bits":130,"color":"FF0000","speed":5,"delay":50},
            {"led_bits":132,"color":"FF0000","speed":5,"delay":50},{"led_bits":136,"color":"FF0000","speed":5,"delay":50},
            {"led_bits":144,"color":"FF0000","speed":5,"delay":50},{"led_bits":160,"color":"FF0000","speed":5,"delay":50},
            {"led_bits":192,"color":"FF0000","speed":5,"delay":50},{"led_bits":127,"color":"000000","speed":15,"delay":20},
            {"led_bits":127,"color":"FF0000","speed":20,"delay":30},{"led_bits":127,"color":"000000","speed":20,"delay":30},
            {"led_bits":127,"color":"FF0000","speed":20,"delay":30},{"led_bits":127,"color":"000000","speed":20,"delay":30}
        ]
    
    # Save the updated configuration back to the file
    with open(config_path, 'w') as file:
        json.dump(config, file)

def update_led_config(previous_subscriber_count, current_subscriber_count, drive_letter):
    if previous_subscriber_count is None:
        print("Initial setup. Configuring LEDs.")
        configure_leds(True, drive_letter)
    elif previous_subscriber_count == current_subscriber_count:
        print("Subscriber count unchanged.")
    elif current_subscriber_count > previous_subscriber_count:
        print("Increase in subscribers.")
        configure_leds(True, drive_letter)
    elif current_subscriber_count < previous_subscriber_count:
        print("Decrease in subscribers.")
        configure_leds(False, drive_letter)
    
        