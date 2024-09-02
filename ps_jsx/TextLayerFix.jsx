// author: xushiyin
// mobile: 18682193124

// #target photoshop

const TargetName = "价格";
const TargetValue = "589";

// 使用文件对话框选择文件夹
// var folder = Folder.selectDialog("请选择包含图片的文件夹");

//  递归查找指定的文本图层名称，并且设置其文本内容
function traverseLayers(layers) {
    for (let i = 0; i < layers.length; i++) {
        const layer = layers[i];
        if (layer.typename === "LayerSet") {
            traverseLayers(layer.layers);
        } else {
            if (layer.kind === LayerKind.TEXT && layer.name === TargetName) {
                layer.textItem.contents = TargetValue;
            }
        }
    }
}

function main() {
    const filePath = "C:/Users/Achil/Desktop/testPsds/664392289951.psd";
    const fileRef = new File(filePath);
    const doc = app.open(fileRef);
    traverseLayers(doc.layers);
    doc.save();
    doc.close();
}

main();

