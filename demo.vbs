Dim speaks, speech
    speaks="0"
    Set speech=CreateObject("sapi.spvoice")
    speech.Speak speaks
    with speech
    .Volume = 100
    .Rate = 4
    end with