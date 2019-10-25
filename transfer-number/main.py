from twilio.rest import Client
import os


def transfer_number(
    number_sid,
    from_account_sid,
    to_account_sid,
    address_sid,
    trunk_sid,
    auth_token,
    to_account_auth_token,
):
    client = Client(from_account_sid, auth_token)
    incoming_phone_number = client.incoming_phone_numbers(phone_number_sid).update(
        account_sid=to_account_sid, address_sid=address_sid
    )
    print(
        "Transferred {} from {} to {}".format(
            incoming_phone_number.phone_number, from_account_sid, to_account_sid
        )
    )

    client = Client(to_account_sid, to_account_auth_token)
    client.incoming_phone_numbers(phone_number_sid).update(trunk_sid=trunk_sid)
    print(
        "Set trunk for {} to {}".format(incoming_phone_number.phone_number, trunk_sid)
    )


if __name__ == "__main__":
    from_account_sid = os.environ["FROM_ACCOUNT_SID"]
    to_account_sid = os.environ["TO_ACCOUNT_SID"]
    auth_token = os.environ["AUTH_TOKEN"]
    phone_number_sid = os.environ["PHONE_NUMBER_SID"]
    address_sid = os.environ["ADDRESS_SID"]
    trunk_sid = os.environ["TRUNK_SID"]
    to_account_auth_token = os.environ["TO_ACCOUNT_AUTH_TOKEN"]
    
    transfer_number(
        phone_number_sid,
        from_account_sid,
        to_account_sid,
        address_sid,
        trunk_sid,
        auth_token,
        to_account_auth_token,
    )
