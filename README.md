first, use client=shocky.initilize_shocky() to initilize the device, and use random to generate a key.

if you are not using the default esp firmware, or have changed the mdns url, run shocky.change_url(yourURL)
(note you MUST use http:// in the string)

for use with server:
    use shocky.init_subscriber(client, key)  to receive connections over the internet from the server with the key

    if you use init_subscriber, put shocky.start_loop(client) to poll the server repeatedly and put shocky.stop_loop(client) to end the polling once your done

    use shocky.send_shock_wan(client, key, power, duration) or shocky.send_shock_wan(client, key, power, duration) to send a shock over the internet the client with key

    to stop over the internet, use shocky.estop_wan(client,key)

for use within local netowrk:
    use shocky.send_shock(url, power, duration) to send a shock locally

    use shocky.send_vibration(url, power, duration) to send a vibration locally

    to stop on a local network, run shocky.estop(url)






