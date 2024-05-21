from requests import post

single = ["s","S"]
double = ["d","D"]

def POST(MODE,DIFF,SONG,SCORE,PLATE,AUTH):
    if MODE in single:
        MODE = "Single"
    elif MODE in double:
        MODE = "Doube"
    hold = str(PLATE)
    PLATE = hold.capitalize()

    submitdict = {
        "songName":f"{SONG}",
        "chartType":f"{MODE}",
        "chartLevel":f'{DIFF}',
        "plate":f"{PLATE}Game",
        "score":f"{SCORE}",
        "isBroken":False
    } #someone better not fuck this up for everyone
    response = post("https://piuscores.arroweclip.se/api/phoenixScores?KeepBestStats=false",
                    headers={
                        'accept':'*/*',
                        'Authorization':f"{AUTH}"
                    },
                    json=submitdict
                    )
    responsecode = response.status_code
    if responsecode == 200:
        respond = "Score Submitted!"
    if responsecode == 400:
        respond = "Score not submitted, maybe try re entering your Authorization header"
    return respond

if __name__ == "__main__":
    POST("s","17","Achluoias","0111111","Fair","Basic OmE5NDY3OWU5LTE5OTItNDcyOS1hMzI3LTBmMGRkYjc5N2EzZA==")