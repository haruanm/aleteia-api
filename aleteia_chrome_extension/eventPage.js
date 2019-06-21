var menuId = "aleteia";

var contextMenuItem = {
  id: menuId,
  title: "Aleteia",
  contexts: ["selection"],
};

chrome.runtime.onInstalled.addListener(function () {
  chrome.contextMenus.create(contextMenuItem);
});

chrome.contextMenus.onClicked.addListener(function (clickAleteia) {
  if (clickAleteia.menuItemId == menuId) {
    getValues();
  }
});
