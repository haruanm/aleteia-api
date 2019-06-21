function getValues() {
  chrome.tabs.query({ 'active': true, 'currentWindow': true }, function (tabs) {
    url = tabs[0].url;
    chrome.tabs.executeScript({
      code: "window.getSelection().toString();"
    }, function (selection) {
      text = selection;
      sendLoadingNotification(text, url, loadingCallback);
    });
  });
}

function sendLoadingNotification(text, url, callback) {
  chrome.notifications.clear("Notification");
  const notification = {
    type: "basic",
    iconUrl: "images/aleteia128.png",
    title: "Carregando...",
    message: 'Estamos avaliando sua notícia. Você terá o resultado em alguns instantes :D '
  }

  chrome.notifications.create("Notification", notification, () => loadingCallback(text, url));
};

function loadingCallback(text, url) {
  fetch('http://localhost:8000/api/v1/', {
    method: 'post',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json; charset=utf-8'
    },
    body: JSON.stringify({
      url: url,
      text: text[0]
    })
  }).then(res => res.json())
    .then(res => {
     
      let message = 'Esta notícia provavelmente é verdadeira.'
      if (res.response !== 'True') {
        message = 'Esta notícia parece ser falsa, vale dar mais uma pesquisada.'
      }

      const notificationOption = {
        type: "basic",
        iconUrl: "images/aleteia128.png",
        title: "Resultado:",
        message: message,
        requireInteraction: true,
        priority: 2,
      }
      console.table(res);

      chrome.notifications.create("Notification", notificationOption);

    })
    .catch(error => {
      console.error(error)

      const notificationOption = {
        type: "basic",
        iconUrl: "images/aleteia128.png",
        title: "Ops!",
        message: 'Ocorreu um erro ao enviar a sua solicitação! Verifique sua conexão com a internet e tente novamente!',
        requireInteraction: true,
        priority: 0
      }
      chrome.notifications.create("Notification", notificationOption);
    });
};

