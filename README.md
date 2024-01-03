<hr>
<div align="center">
  <img height="100%" src="https://github.com/isaaclins/SlytherCord/assets/104733575/16c46186-c233-41c7-b4ac-69a80fe97571"  />
</div>
<hr>



  # Discord Python RAT Documentation

## Introduction

The Discord Python RAT (Remote Administration Tool) is a project designed to provide remote administration capabilities using Discord as the communication platform. It leverages the Discord Bot API to manage and control a system remotely through various commands. This document aims to explain the functionalities of each module (feature) and provide examples of how to use them.

## Table of Contents

1. [Command List](#command-list)
2. [Modules](#modules)
   - [.help](#help)
   - [.ping](#ping)
   - [.cd \<directory\>](#change-directory)
   - [.ls](#list-directory)
   - [.export \<file\>](#export-file-into-link)
   - [.upload \<link\>](#upload-file-from-link)
   - [.cmd \<cmd\>](#execute-cmd-command)
   - [.run \<file\>](#run-a-file)
   - [.ss](#take-a-screenshot-of-the-first-monitor)
   - [.blue](#send-a-bluescreen)
   - [.start](#add-the-bot-to-the-startup-directory)
   - [.exit](#close-the-connection-to-the-bot)
   - [.reload](#reload-the-connection-to-the-bot)
   - [.volumeup](#increase-the-volume)
   - [.volumedown](#decrease-the-volume)
   - [.admincheck](#check-admin-privileges)
   - [.location](#get-location-information)
   - [.clipboard](#get-clipboard-content)
   - [.wallpaper](#change-wallpaper)
   - [.export](#export-file-into-link)
   - [.upload](#upload-file-from-link)
   - [.shell](#execute-shell-command)
   - [.run](#run-command)
   - [.cd](#change-directory)
   - [.input](#send-keystrokes)
   - [.type](#type-text)
   - [.say](#text-to-speech)
   - [.message](#display-message-box)
   - [.mouse](#display-mouse-grid)

## Command List<a name="command-list"></a>

```
.help               - Shows this message
.ping               - Latency delay of the bot
.cd <directory>     - Change Directory
.ls                 - List Directory
.export <file>      - Export File into link
.upload <link>      - Upload File from link
.cmd <cmd>          - Execute CMD Command
.run <file>         - Run a File
.ss                 - Take a Screenshot of the first monitor
.blue               - Sends a bluescreen ;)
.start              - Adds the bot to the startup directory
.exit               - Closes the connection to the bot
.reload             - Reloads the connection to the bot
.volumeup           - Increase the system volume
.volumedown         - Decrease the system volume
.admincheck         - Check admin privileges
.location           - Get location information
.clipboard          - Get clipboard content
.wallpaper          - Change wallpaper
.export             - Export file into link
.upload             - Upload file from link
.shell              - Execute shell command
.run                - Run command
.cd                 - Change directory
.input              - Send keystrokes
.type               - Type text
.say                - Text to speech
.message            - Display message box
.mouse              - Display mouse grid
```

## Modules<a name="modules"></a>

### .help<a name="help"></a>

Displays a list of available commands with their descriptions.

**Example:**
```
.help
```

### .ping<a name="ping"></a>

Shows the latency delay of the bot in milliseconds.

**Example:**
```
.ping
```

### .cd \<directory\><a name="change-directory"></a>

Change the current working directory.

**Example:**
```
.cd C:\Users\Username\Documents
```

### .ls<a name="list-directory"></a>

List files in the current directory.

**Example:**
```
.ls
```

### .export \<file\><a name="export-file-into-link"></a>

Export a file and provide a link.

**Example:**
```
.export example.txt
```

### .upload \<link\><a name="upload-file-from-link"></a>

Upload a file from a provided link.

**Example:**
```
.upload https://example.com/file.txt
```

### .cmd \<cmd\><a name="execute-cmd-command"></a>

Execute a command using CMD.

**Example:**
```
.cmd ipconfig
```

### .run \<file\><a name="run-a-file"></a>

Run an executable file.

**Example:**
```
.run program.exe
```

### .ss<a name="take-a-screenshot-of-the-first-monitor"></a>

Take a screenshot of the first monitor.

**Example:**
```
.ss
```

### .blue<a name="send-a-bluescreen"></a>

Trigger a bluescreen on the system.

**Example:**
```
.blue
```

### .start<a name="add-the-bot-to-the-startup-directory"></a>

Add the bot to the system's startup directory.

**Example:**
```
.start
```

### .exit<a name="close-the-connection-to-the-bot"></a>

Close the connection to the bot.

**Example:**
```
.exit
```

### .reload<a name="reload-the-connection-to-the-bot"></a>

Reload the connection to the bot.

**Example:**
```
.reload
```

### .volumeup<a name="increase-the-volume"></a>

Increase the system volume to 100%.

**Example:**
```
.volumeup
```

### .volumedown<a name="decrease-the-volume"></a>

Decrease the system volume to 0%.

**Example:**
```
.volumedown
```

### .admincheck<a name="check-admin-privileges"></a>

Check if the bot has admin privileges.

**Example:**
```
.admincheck
```

### .location<a name="get-location-information"></a>

Get the current geolocation information.

**Example:**
```
.location
```

### .clipboard<a name="get-clipboard-content"></a>

Get the content of the system clipboard.

**Example:**
```
.clipboard
```

### .wallpaper<a name="change-wallpaper"></a>

Change the system wallpaper.

**Example:**
```
.wallpaper
```

### .input<a name="send-keystrokes"></a>

Send a combination of keystrokes.

**Example:**
```
.input Ctrl Alt Delete
```

### .type<a name="type-text"></a>

Type specified text as if it were typed by a keyboard.

**Example:**
```
.type Hello, Discord!
```

### .say<a name="text-to-speech"></a>

Convert text to speech and play it.

**Example:**
```
.say Hello, Discord!
```
### .shell<a name="execute-shell-command"></a>

Execute a shell command on the system.

**Example:**
```
.shell dir
```

### .run<a name="run-command"></a>

Run a command on the system using subprocess.

**Example:**
```
.run notepad.exe
```

Thank you for pointing that out, and I appreciate your understanding. If you have any more questions or need further clarification, feel free to ask!

### .message<a name="display-message-box"></a>

Display a message box on the system.

**Example:**
```
.message This is an important message!
```

### .mouse<a name="display-mouse-grid"></a>

Display a grid on the screen to help locate the mouse pointer.

**Example:**
```
.mouse large
```

**Note:** The `large` argument specifies the size of

 the grid (`large`, `medium`, `small`, `tiny`).

## Conclusion

This documentation provides an overview of the Discord Python RAT and its available features. It is important to use these functionalities responsibly and in compliance with relevant laws and regulations. Always ensure that you have appropriate authorization before remotely administering systems.
