const { app, BrowserWindow, ipcMain} = require('electron')

let win

function createWindow () {

    // Créer le browser window.
    win = new BrowserWindow({
        width: 800,
        height: 580,
        webPreferences: {
        nodeIntegration: true
      }
    })

    // Dans le processus principal .
    ipcMain.on('sync', (event, arg) => {
        event.returnValue = 'Sam'
    })

    // and load the index.html of the app.
    win.loadFile('index.html')

    // Ouvre les DevTools.
    win.webContents.openDevTools()

    // Émit lorsque la fenêtre est fermée.
    win.on('closed', () => {win = null})
}

app.on('ready', createWindow)

// Quitte l'application quand toutes les fenêtres sont fermées.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (win === null) {
    createWindow()
  }
})