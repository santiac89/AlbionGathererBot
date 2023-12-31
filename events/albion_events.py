from enum import Enum

class AlbionEvents(Enum):
    # 12:637993823308929158 18:[] 19:[-63 68 12 104 -29 1 114 78 -91 -75 -21 68 -13 -96 -29 -67] 20:[-23 20 93 -6 73 127 19 78 -65 44 -42 65 -97 105 -82 -16] 21:25900 22:0 23:3 24:-1 252:89]
    AccessStatus = 197
    AchievementProgressInfo = 143
    ActionOnBuildingCancel = 60
    ActionOnBuildingFinished = 61 # Repear: [60]evInstallResourceCancel - map[0:1562 1:63802829 282167 2:442 3:454 4:2 252:60] 0: UserObjectId, 2: ActionId, 4: ActionType
    ActionOnBuildingStart = 59 
    ActiveMatchUpdate = 119
    ActiveSpellEffectsUpdate = 10
    ArenaRegistrationInfo = 255
    AttachItemContainer = 94 #  map[0:78 1:[-99 -50 125 -49 86 0 -115 74 -74 67 9 101 -87 -71 -66 -10] 3:[0 0 0 0 0 0 656 657] 4:8 252:89] (0: ObjectId, 3: ItemId[])
    Attack = 12
    AttackBuilding = 22
    AvatarUnlocked = 389
    BankVaultInfo = 400 # map[0:6 1:6466931c-65a1-4c5d-870b-8724cf2611dc@3007 2:[] 3:[] 4:[] 5:[] 6:[] 7:[] 8:[] 252:390]
    BaseVaultInfo = 399
    BoostFarmable = 305
    CastCancel = 15
    CastFinished = 17
    CastHit = 19
    CastHits = 20
    CastlePhaseChanged = 404
    CastSpell = 18
    CastStart = 13
    CastTimeUpdate = 16
    ChallengePoints = 356
    ChangeAvatar = 151
    ChangeEquipment = 4
    ChangeFlaggingFinished = 342
    ChangeMountSkin = 152
    ChannelingEnded = 21
    ChannelingUpdate = 14
    CharacterEquipmentChanged = 85 # map[0:297 1:26283117 2:[0 1721 0 0 0 2330 2301 2468 0 0] 5:[-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 3168] 252:85]
    CharacterStats = 136
    CharacterStatsDeathHistory = 138
    CharacterStatsKillHistory  = 137
    ChatMessage = 70
    ChatMuted   = 73
    ChatSay = 71
    ChatWhisper = 72
    ClaimOrbCancel = 125
    ClaimOrbFinished   = 124
    ClaimOrbStart   = 123
    Cloak = 215
    ClusterInfoUpdate = 133
    ConsoleEvent = 149
    ConstructionSiteInfo    = 44
    CraftBuildingInfo   = 41
    CraftingFocusUpdate = 9
    CraftItemFinished   = 68
    CrystalRealmFeedback = 362
    CustomizationChanged = 390
    DamageShieldUpdate = 8
    DebugAggroInfo = 118
    DebugDiminishingReturnInfo  = 121
    DebugDrawEvent = 318
    DebugReputationInfo = 120
    DebugSmartClusterQueueInfo = 122
    DebugVariablesInfo = 119
    DefenseUnitAttackBegin = 291
    DefenseUnitAttackDamage = 293
    DefenseUnitAttackEnd = 292
    DetachItemContainer = 95 #  map[0:[-95 72 -77 -75 -70 34 127 73 -114 -96 28 8 75 -107 -106 125] 252:90]
    Died = 156
    DuelDenied = 176
    DuelEnded = 175
    DuelLeftArea = 177
    DuellingChallengePlayer = 172
    DuelReEnteredArea = 178
    DuelStarted = 174
    DurabilityChanged = 92
    EasyAntiCheatKick = 387
    EasyAntiCheatMessageToClient = 357
    EndArenaMatch = 117
    EndTerritoryMatch = 116
    EnergyUpdate = 7
    EnteringArenaCancel = 257
    EnteringArenaLockCancel = 259
    EnteringArenaLockStart = 258
    EnteringArenaStart = 256
    EnteringExpeditionCancel = 253
    EnteringExpeditionStart = 252
    EventCode379 = 379
    ExitEnterCancel = 241
    ExitEnterFinished = 242
    ExitEnterStart = 240
    ExpeditionQuestProgressInfo = 249
    ExpeditionRegistrationInfo = 251
    ExpeditionStartent = 301
    FactionBuildingInfo = 40
    FarmableObjectInfo = 188
    FarmBuildingInfo    = 46
    FinishedAchievement = 142
    FishingCancel = 336
    FishingCast = 333
    FishingCatch = 334
    FishingFinished = 335
    FishingMiniGame = 339
    FishingStart = 332
    ForcedMovement = 134
    ForcedMovementCancel    = 135
    FriendInfos = 282
    FriendOnlineStatus = 284
    FriendRemoved = 286
    FriendRequest = 280
    FriendRequestAnswered   = 283
    FriendRequestCanceled = 285
    FriendRequestInfos  = 281
    FriendUpdated = 287
    FullAchievementInfo = 141
    FullAchievementProgressInfo = 144
    FullAutoLearnAchievementInfo = 146
    FullExpeditionInfo = 248
    FullQuestInfo = 245
    FullTrackedAchievementInfo = 145
    FurnitureObjectBuffProviderInfo = 186
    FurnitureObjectCheatProviderInfo = 187
    GameEvent = 153
    GrabbedLoot = 264 # LOOT: map[0:424 1:Triky313 2:Bruno313 4:1841 5:1 252:256] | SILVER: map[0:6436 2:Triky313 3:true 5:1550115 252:256] (0: ObjectId, 1: LootedBody, 2: Looter, 4: ItemId, 5: Quantity) 
    GuildAccessTagUpdated = 328
    GuildAccountLogEvent = 405
    GuildFullAccessTagsUpdated  = 327
    GuildLogoChanged = 183
    GuildLogoObjectUpdate = 191
    GuildLogoUpdate = 182
    GuildMemberTerritoryUpdate = 131
    GuildMemberWorldUpdate = 101
    GuildPlayerUpdated = 99
    GuildStats = 139
    GuildUpdate = 98
    GuildVaultInfo = 398
    GvgSeasonCheatCommand = 330
    GvgSeasonUpdate     = 329
    HarvestableChangeState  = 38
    HarvestCancel = 52
    HarvestFinished = 57 # map[0:5270 1:637926215956544319 2:637926215972723131 3:4250 4:1 5:1 7:28 8:[] 9:[] 252:54] - 0: UserId, 3: ObjectId, 4:ItemId 5: Res Standard Quantity 6: Sammelbonus Res, 6: Premium Bonus Res, 8: Inhalt in der Ressource
    HarvestStart = 51 # map[0:5270 1:637926215956544319 2:637926215956544319 3:4250 4:16 5:1.6169999 6:5287 7:2195 252:52] - 0 = UserId, 3 = ObjectId, 5: Abbauzeit 7: Abbau-Tool (T8_2H_TOOL_SICKLE), 
    HealthUpdate = 6
    HellClusterTimeUpdate = 243
    HideoutManagementUpdate = 412
    HideoutObjectUpdate = 431
    InCombatStateUpdate = 263 # map[0:671362 1:true 2:true 252:257] | 1 = true; player hits enemy | 2 = true; enemy hits player
    InitHideoutAttackCancel = 410
    InitHideoutAttackFinished = 411
    InitHideoutAttackStart = 409
    InstallResourceCancel   = 66
    InstallResourceFinished = 67
    InstallResourceStart    = 65
    InvalidateItemContainer = 96
    InventoryDeleteItem = 26, # map[0:754 1:48 252:24] (0: ObjectId) 
    InventoryPutItem = 25, #  map[0:652 1:6 2:[118 -97 114 112 -46 84 -60 75 -103 -93 -3 -29 118 -125 -50 96] 3:17 252:23] (0: ObjectId, 1: Inventory slot (no value is slot 0), 2: InteractGuid)
    InvitationPlayerTrade = 164
    InvitedMercenaryToMatch = 132
    InvitedToArenaMatch = 260
    InvitedToExpedition = 250
    InvitedToGuild = 100
    IpChanged = 413
    ItemRerollQualityCancel = 63
    ItemRerollQualityFinished = 64
    ItemRerollQualityStart = 62
    JoinedChatChannel = 194
    JoinFinished = 1, # <- UserInfo
    JournalFillError = 279
    JournalGotFull = 278
    KilledPlayer = 154
    KillHistoryDetails = 140
    KnockedDown = 157
    LaborerGotUpgraded = 277
    LaborerObjectInfo   = 48
    LaborerObjectJobInfo    = 49
    Leave = 1
    LeftChatChannel = 195
    LockItemContainer  = 97
    LogoutCancel    = 69
    LootChestOpened = 380 # map[0:23 252:369]
    LootEquipmentChanged = 208
    MarketPlaceBuildingInfo = 50
    MarketPlaceNotification = 171
    MatchLootChestOpeningCancel = 360
    MatchLootChestOpeningFinished = 359
    MatchLootChestOpeningStart = 358
    MatchPlayerChangedAvatarEvent = 163
    MatchPlayerJoinedEvent = 158
    MatchPlayerMainGearStatsEvent = 162
    MatchPlayerStatsCompleteEvent = 160
    MatchPlayerStatsEvent = 159
    MatchTimeLineEventEvent = 161
    MatchUpdate = 118
    MeldBuildingInfo    = 43
    MightFavorPoints = 480 # map[0:63063 2:21021 3:16617 5:5539 6:3
    MiniMapOwnedBuildingsPositions = 180
    MiniMapPing = 170
    MinimapSmartClusterZergs = 314
    MinimapZergs = 313
    MobChangeState  = 39
    Mount = 200
    MountCooldownUpdate = 298
    MountHealthUpdate = 297
    Move = 2
    MutePlayerUpdate = 384
    NewArenaAgent = 304
    NewArenaExit = 130
    NewBuilding = 37
    NewCastleObject = 107
    NewChainSpell = 110
    NewCharacter = 27
    NewChatChannels = 193
    NewDuellingPost = 173
    NewDynamicGuildLogo = 367
    NewEquipmentItem = 28, #  map[0:657 1:2036 2:1 4:28169331 5:Apolo540 6:3 7:90000000 8:[] 9:[0] 252:27] (0: ObjectId, 1: ItemId, 2: Amount, 4: Est. market value, 5: CrafterName)
    NewExit = 203
    NewExpeditionAgent = 299
    NewExpeditionCheckPoint = 300
    NewExpeditionExit = 238
    NewExpeditionNarrator = 239
    NewFishingZoneObject = 338
    NewFloatObject = 337
    NewFurnitureItem = 30
    NewHarvestableObject = 35 # map[0:[3405 3468] 1:[6 6] 2:[3 2] 3:[182 -383 176 -369 183 -371] 4:[3 3] 252:35] - 0: ObjectId 2: Max charges, 4: Current charges
    NewHellgate = 236
    NewHellgateExit = 237
    NewHideoutExit = 408 
    NewHideoutManagement = 407
    NewHideoutObject = 406
    NewHomeObject = 430
    NewInformationProvider = 366
    NewIslandAccessPoint = 202
    NewIslandManagement = 213
    NewJournalItem = 31
    NewLaborerItem = 32, # [0:513 1:7996 2:4 4:522947156 5: 6:10000 7:72000000 252:32]
    NewLocationMarker = 363
    NewLoot = 93 # map[0:1863 2:1853 3:Dicky 4:[236.79169 -185.40233] 5:42.864536 6:true 7:1 10:[[-85 -58 82 55 101 -15 76 79 -103 -113 -21 8 -33 46 -99 -28]] 
    NewLootChest = 378 # map[0:23 1:[20.5 177.5] 2:423 3:KEEPER_SOLO_BOOKCHEST_STANDARD 4:FOREST_GREEN_LOOTCHEST_KEEPER_SOLO_BOOKCHEST_STANDARD 5:4 6:637734315213820408 7:[] 8:[] 13:true 252:367] # map[0:4399 1:[165 -263] 3:TREASURE_SOLO_UNCOMMON 4:SWAMP_DEAD_LOOTCHEST_TREASURE_SOLO_UNCOMMON 5:4 6:637926439332719127 7:[] 8:[] 13:true 14:SWAMP_DEAD_TREASURE_SOLO 16:31ff503a-ded6-53d6-974a-7e32e3126457 252:370]
    NewMatchLootChestObject = 129
    NewMob = 117
    NewMonolithObject = 104
    NewMountObject = 296
    NewOrbObject = 106
    NewOutpostObject = 343
    NewPortalEntrance = 307
    NewPortalExit = 308
    NewQuestGiverObject = 244
    NewRandomDungeonExit = 309
    NewRandomResourceBlocker = 429
    NewRealEstate = 179
    NewShrine = 382 # map[0:19 1:[-89 90] 2:180 3:GENERAL_SHRINE_COMBAT_BUFF 4:SHRINE_NON_COMBAT_BUFF 5:1 6:637734312344532502 252:371]
    NewSiegeCampObject = 105
    NewSilverObject = 36
    NewSimpleHarvestableObject = 33
    NewSimpleHarvestableObjectList = 34
    NewSimpleItem = 29, #  map[0:505 1:7006 2:1 3:true 4:29033970 252:27] (0: ObjectId, 1: ItemId, 2: Amount, 4: Est. market value)
    NewSpellEffectArea = 108
    NewTeleportStone = 214
    NewTileSwitch = 365
    NewTravelpoint = 201
    NewTreasureChest = 112
    NewTutorialBlocker = 364
    NewUnlockedPersonalSeasonRewards = 354
    NewUnreadMails = 189
    NewWarCampObject = 128
    NotifyCrystalMatchReward = 361
    ObjectEvent = 103
    ObserveStart = 312
    OpenWorldAttackConquerCancel = 425
    OpenWorldAttackConquerFinished = 424
    OpenWorldAttackConquerStart     = 423
    OpenWorldAttackConquerStatus = 426
    OpenWorldAttackEnd = 428
    OpenWorldAttackScheduleCancel = 422
    OpenWorldAttackScheduleFinished = 421
    OpenWorldAttackScheduleStart = 420
    OpenWorldAttackStart = 427
    OrbClaimed = 127
    OrbUpdate  = 126
    OtherGrabbedLoot = 262
    OutpostClaimed = 345
    OutpostReward = 346
    OutpostUpdate = 344
    OverChargeEnd = 347
    OverChargeStatus = 348
    OverloadModeUpdate = 317
    PartyChangedOrder = 220 # map[0:14368 2:1 3:[-45 -35 124 14 -23 103 -41 74 -71 66 67 20 -12 60 44 -101] 4:[[-45 -35 124 14 -23 103 -41 74 -71 66 67 20 -12 60 44 -101] [-118 61 -70 72 17 -107 121 72 -102 110 20 -25 64 20 106 2]] 5:[Triky313 Bruno313] 6:[0 0] 7:[18 0] 8:[35 0] 9:[-1 -1] 10:[true true] 252:212]
    PartyDisbanded = 221 # map[1:14184 252:213]
    PartyFinderApplicantsUpdate = 351
    PartyFinderEquipmentSnapshot = 352
    PartyFinderFullUpdate = 349
    PartyFinderJoinRequestDeclined = 353
    PartyFinderUpdate = 350
    PartyInvitation = 216
    PartyInvitationPlayerBusy = 230 
    PartyJoined = 217
    PartyJoinRequest = 234
    PartyLeaderChanged = 225 # map[0:14595 1:[-45 -35 124 14 -23 103 -41 74 -71 66 67 20 -12 60 44 -101] 252:217]
    PartyLootItems  = 288 
    PartyLootItemsRemoved = 289 
    PartyLootSettingChangedPlayer = 226 # map[0:14368 1:1 252:218]
    PartyMarkedObjectsUpdated = 231
    PartyOnClusterPartyJoined = 232
    PartyPlayerJoined = 222 # map[0:11925 1:[-63 -19 39 16 26 35 -25 67 -111 60 -87 -58 -31 -100 -124 -44] 2:Mitch77 3:1 4:20 5:12 6:-1 7:true 252:214]
    PartyPlayerLeft = 224 # map[0:14368 1:[-45 -35 124 14 -23 103 -41 74 -71 66 67 20 -12 60 44 -101] 252:216]
    PartyPlayerUpdated = 229 # map[0:Bruno313 1:true 3:5 252:221]
    PartySetRoleFlag = 233 # map[0:8 1:[-118 61 -70 72 17 -107 121 72 -102 110 20 -25 64 20 106 2] 252:225] (0: FlagType, 1: ObjectId)
    PartySilverGained = 227 
    PaymentTransactions = 315
    PerformanceStatsUpdate = 316
    PersonalSeasonPointsGained = 355
    PlaceableObjectPlace = 184
    PlaceableObjectPlaceCancel = 185
    PlayEmote   = 74
    PlayerBuildingInfo  = 45
    PlayerCounts = 261
    PlayerMovementRateUpdate = 311
    PlayerTradeAcceptChange = 169
    PlayerTradeCancel = 166
    PlayerTradeFinished = 168
    PlayerTradeStart = 165
    PlayerTradeUpdate = 167
    PremiumChanged = 274
    PremiumExtended = 275
    PremiumLifeTimeRewardGained = 276
    QuestGiverDebugInfo = 148
    QuestGiverInfoForPlayer = 247
    QuestGiverQuestOffered = 147
    QuestProgressInfo = 246
    RandomDungeonPositionInfo = 370
    Ratingent = 303
    RealEstateListUpdate = 181
    ReceivedSeasonPoints = 418
    RecordCameraMove = 319
    RecordStart = 320
    RecoveryVaultGuildInfo = 402
    RecoveryVaultPlayerInfo = 401
    RegenerationCraftingChanged = 89
    RegenerationEnergyChanged = 87
    RegenerationHealthChanged = 86
    RegenerationHealthEnergyComboChanged = 90
    RegenerationMountHealthChanged = 88
    RegenerationPlayerComboChanged = 91
    RemovedChatChannel = 196
    RepairBuildingInfo      = 42
    ReputationImplicationUpdate = 295
    ReputationUpdate = 290
    ResetCooldowns = 11
    Respawn = 83
    ResurrectionOffer = 206
    ResurrectionReply = 207
    RewardGranted = 254
    SeasonPointsByKillingBooster = 331
    ServerDebugLog = 84
    ShopTileUpdate = 385
    ShopUpdate = 386
    SiegeCampClaimCancel = 266
    SiegeCampClaimFinished = 267
    SiegeCampClaimStart = 265
    SiegeCampScheduleResult = 268 
    SmartClusterQueueActiveInfo = 415
    SmartClusterQueueInvite = 417
    SmartClusterQueueKickWarning = 416
    SmartClusterQueueUpdateInfo = 414
    SpellCooldownUpdate  = 235
    StartArenaMatchInfos = 115
    StartDeterministicRoam = 326
    StartLogout = 192
    StartMatch = 113
    StartTerritoryMatchInfos = 114
    SteamAchievementCompleted = 340
    StopEmote   = 75
    SystemMessage   = 76
    TakeSilver = 58 # map[0:-57 1:2178162 2:-57 3:10000000 8:10000 252:55]
    Teleport = 3
    TerritoryBonusLevelUpdate = 419
    TerritoryClaimCancel = 322
    TerritoryClaimFinished = 323
    TerritoryClaimStart = 321
    TerritoryScheduleResult = 324
    TimeSync = 150
    TreasureChestForceCloseInventory = 273
    TreasureChestUsingCancel = 271
    TreasureChestUsingFinished = 270
    TreasureChestUsingOpeningComplete = 272
    TreasureChestUsingStart = 269
    TriggerHintBox = 369
    TutorialBuildingInfo    = 47
    TutorialUpdate = 368
    Unknown187 = 190
    Unknown408 = 433
    Unknown409 = 434
    Unknown410 = 435
    Unknown411 = 436
    Unknown412 = 437
    Unknown413 = 438
    Unknown414 = 439
    Unknown415 = 440
    Unknown416 = 441
    Unknown417 = 442
    Unknown418 = 443
    Unknown419 = 444
    Unknown420 = 445
    Unknown421 = 446
    Unknown422 = 447
    Unknown478 = 478
    UnlockVanityUnlock = 388
    UnrestrictedPvpZoneUpdate = 294
    Unused = 0
    UpdateAccountState  = 325
    UpdateBrecilienStanding = 82 # map[0:11575080 1:3858360 2:970279167 252:81] 0: StandingPoints
    UpdateChainSpell = 111
    UpdateChatSettings = 205
    UpdateCurrency = 80
    UpdateFactionStanding = 81
    UpdateFame = 77 # map[0:4195 1:5811910006347 2:100000000 4:10000 6:1 7:427 252:72] (0: ObjectId, 1: TotalPlayerFame, 2: fameWithZoneMultiplier, 3: GroupSize, 4: Multiplier, 5: IsPremiumBonus, 6: BonusFactor, 8: UsedBagInsightItemIndex, 10: SatchelFame, )
    UpdateHome = 204
    UpdateInfamy = 432
    UpdateLearningPoints = 78
    UpdateLootChest = 379 # 0=ObjectId, 3=PlayerGuid, 4=PlayerGuid, 7=Free4All map[0:4769 1:5 2:637927794424868192 3:[[-45 -35 124 14 -23 103 -41 74 -71 66 67 20 -12 60 44 -101]] 4:[[-45 -35 124 14 -23 103 -41 74 -71 66 67 20 -12 60 44 -101]] 6:true 7:true 8:2.6 9:true 252:371]
    UpdateMatchDetails = 102
    UpdatePuppet = 341
    UpdateReSpecPoints = 79 # map[0:[0 55814284204 0 0 0] 1:1 2:9948534 3:10000000 252:78] 2: GainedReSpec, 3: PaidSilver
    UpdateShrine = 383 # map[0:19 1:2 2:637734313445294913 252:372]
    UpdateSilver = 76 # map[0:4195 1:884995625105 252:71] (0: ObjectId, 1: CurrentSilver)
    UpdateSpellEffectArea = 109
    UpdateUnlockedAvatarRings = 211
    UpdateUnlockedAvatars = 210
    UpdateUnlockedBuildings = 212
    UpdateUnlockedGuildLogos = 209
    UpdateWardrobe = 403
    UseFunction = 306
    UtilityTextMessage  = 77
    Voteent = 302
    WaitingQueueUpdate = 310
    X_Mounted_X = 198
    X_MountStart = 199
    
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_ 