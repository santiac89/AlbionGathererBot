class JoinOperation():
    def __init__(self, parameters):
        self.UserObjectId = 0
        self.UserGuid = 0
        self.Username = 0
        self.MapIndex = 0
        self.MapGuid = 0
        self.MapType = 0
        self.CurrentFocusPoints = 0
        self.MaxCurrentFocusPoints = 0
        self.LearningPoints = 0
        self.Reputation = 0
        self.ReSpecPoints = 0
        self.Silver = 0
        self.Gold = 0
        self.InteractGuid = 0
        self.GuildName = 0
        self.MainMapIndex= 0
        self.PlayTimeInSeconds = 0
        self.AllianceName = 0
        self.IsReSpecActive = 0

        if 0 in parameters: 
            self.UserObjectId = parameters[0]

        if 1 in parameters: 
            self.UserGuid = parameters[1]

        if 2 in parameters: 
            self.Username = parameters[2]

        if 8 in parameters: 
            self.MapIndex = parameters[8]
            # MapType = WorldData.GetMapType(MapIndex);
            # MapGuid = WorldData.GetMapGuid(MapIndex);

    #     if 23 in parameters:
    #         CurrentFocusPoints = parameters[23].ObjectToDouble();

    #     if 24 in parameters:  
    #         MaxCurrentFocusPoints = parameters[24].ObjectToDouble();

    #     if 28 in parameters:  
    #         Silver = FixPoint.FromInternalValue(parameters[28].ObjectToLong() ?? 0);

    #     if 29 in parameters:  
    #         Gold = FixPoint.FromInternalValue(parameters[29].ObjectToLong() ?? 0);

    #     if 32 in parameters:  
    #         LearningPoints = FixPoint.FromInternalValue(parameters[32].ObjectToLong() ?? 0);

    #     if 36 in parameters:  
    #         Reputation = parameters[36].ObjectToDouble();

    #     if 38 in parameters && parameters[38] is long[] { Length: > 1 } reSpecArray)
    #     {
    #         ReSpecPoints = FixPoint.FromInternalValue(reSpecArray[1]);
    #     }

    #     if 48 in parameters: 
    #     {
    #         InteractGuid = parameters[48].ObjectToGuid();
    #         ConsoleManager.WriteLineForMessage(MethodBase.GetCurrentMethod()?.DeclaringType, $"Local interact object Guid: {InteractGuid}", ConsoleColorType.EventMapChangeColor);
    #     }

    #     if 52 in parameters: 
    #     {
    #         GuildName = string.IsNullOrEmpty(parameters[52].ToString()) ? string.Empty : parameters[52].ToString();
    #     }

    #     if 59 in parameters: 
    #     {
    #         MainMapIndex = string.IsNullOrEmpty(parameters[59].ToString()) ? string.Empty : parameters[59].ToString();
    #     }

    #     if 62 in parameters: 
    #     {
    #         PlayTimeInSeconds = parameters[62].ObjectToInt();
    #     }

    #     if 72 in parameters: 
    #     {
    #         AllianceName = string.IsNullOrEmpty(parameters[72].ToString()) ? string.Empty : parameters[72].ToString();
    #     }

    #     if 89 in parameters: 
    #     {
    #         IsReSpecActive = parameters[89].ObjectToBool();
    #     }
    # }
