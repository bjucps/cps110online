records = [
    {
        "alm_date": "2015-10-13T00:00:00.000",
        "alm_time": "14:31:08",
        "descript": "Medical assist, assist EMS crew",
        "zip": "06106"
    },
    {
        "alm_date": "2015-10-13T00:00:00.000",
        "alm_time": "03:53:01",
        "descript": "Rescue, EMS incident, other",
        "zip": "06106"
    },
    {
        "alm_date": "2015-10-13T00:00:00.000",
        "alm_time": "15:07:27",
        "descript": "Medical assist, assist EMS crew",
        "zip": "06112"
    }

]

for rec in records:
    print(rec['alm_date'], rec['descript'])

    