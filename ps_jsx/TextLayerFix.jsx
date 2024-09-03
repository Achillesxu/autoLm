// author: xushiyin
// mobile: 18682193124

// #target photoshop

var TargetName = "价格";
var TargetValue = "589";
var TargetFind = false

// 使用文件对话框选择文件夹
// var folder = Folder.selectDialog("请选择包含图片的文件夹");

//  递归查找指定的文本图层名称，并且设置其文本内容
function traverseLayers(layers) {
    for (var i = 0; i < layers.length; i++) {
        var layer = layers[i];
        if (layer.typename === "LayerSet") {
            traverseLayers(layer.layers);
        } else {
            if (layer.kind === LayerKind.TEXT && layer.name === TargetName) {
                layer.textItem.contents = TargetValue;
                TargetFind = true;
            }
        }
    }
}

function parseJSON(jsonString) {
    return eval('(' + jsonString + ')');
}

function readJsonfile() {
    const jsonFile = File.openDialog("请选择JSON文件", "*.json");
    if (jsonFile === null) {
        return null;
    }
       // 打开并读取JSON文件
    jsonFile.open("r");
    var jsonData = jsonFile.read();
    jsonFile.close();
    var data = parseJSON(jsonData);
    return data;
}

function getFileNameWithoutExt(filePath) {
    var fileName = filePath.split('/').pop();
    // 再用 '.' 分割文件名，获取第一个元素（文件名without扩展名）
    return fileName.split('.')[0];
}

function checkAndCreateDir(folderPath) {
    var folder = new Folder(folderPath);

    if (!folder.exists) {
        var result = folder.create();
        if (result) {} else {
            alert("无法创建文件夹: " + folderPath);
        }
    }
}

function saveJpgOptions(quality) {
    var jpegOptions = new JPEGSaveOptions();
    jpegOptions.quality = quality;
    jpegOptions.embedColorProfile = true;
    jpegOptions.formatOptions = FormatOptions.STANDARDBASELINE;
    jpegOptions.matte = MatteType.NONE;
    return jpegOptions;
}


function main() {
    // const filePath = "C:/Users/Achil/Desktop/testPsds/664392289951.psd";
    // const fileRef = new File(filePath);
    // const doc = app.open(fileRef);
    // traverseLayers(doc.layers);
    // doc.save();
    // doc.close();
    var data = readJsonfile();
    if (data === null || data === undefined) {
        alert("未选择文件, 脚本已取消")
        return;
    }
    var outputDir = data["output"]["dir"]
    checkAndCreateDir(outputDir)

    var jpgOpt = saveJpgOptions(data["output"]["quality"])

    var psds = data["psds"];
    for (var key in psds) {
        var fileRef = new File(key);
        var doc = app.open(fileRef);
        var textLayers = psds[key];
        for (var kv in textLayers) {
            TargetName = kv;
            TargetValue = textLayers[kv];
            TargetFind = false;
            traverseLayers(doc.layers);
            if (TargetFind === false) {
                alert("未找到图层: " + TargetName + "请确认！")
            }
        }
        doc.save();
        var psdName = getFileNameWithoutExt(key);
        var saveName = outputDir + "/" + psdName + ".jpg";
        var saveNameFile = new File(saveName);
        doc.saveAs(saveNameFile, jpgOpt, true, Extension.LOWERCASE);
    }
    alert("所有psd文件处理完成, 请检查")
}

main();

