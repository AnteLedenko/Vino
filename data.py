from models import WineList


europe_datastore = {
    '1': WineList("1","Château Margaux","France","Cabernet Sauvignon, Merlot","€840"),
    '2': WineList("2","Sassicaia","Italy","Cabernet Sauvignon, Cabernet Franc","€280"),
    '3': WineList("3","Vega Sicilia Único","Spain","Tempranillo, Cabernet Sauvignon","€370"),
    '4': WineList("4","Dom Pérignon","France","Chardonnay, Pinot Noir","€167"),
    '5': WineList("5","Brunello di Montalcino Biondi-Santi","Italy","Sangiovese","€140"),
    '6': WineList("6","Château d'Yquem","France","Sémillon, Sauvignon Blanc","€370"),
    '7': WineList("7","Tignanello","Italy","Sangiovese, Cabernet Sauvignon","€140"),
    '8': WineList("8","Barolo Monfortino Giacomo Conterno","Italy","Nebbiolo","€651"),
    '9': WineList("9","Hermitage La Chapelle Paul Jaboulet","France","Syrah","€280"),
    '10': WineList("10","Krug Grande Cuvée","France","Pinot Noir, Chardonnay, Pinot Meunier","€158")
}

african_datastore = {
    '11': WineList("1","Kanonkop Paul Sauer","South Africa","Cabernet Sauvignon, Merlot, Cabernet Franc","€56"),
    '12': WineList("2","Rust en Vrede Estate","South Africa","Cabernet Sauvignon, Shiraz, Merlot","€46"),
    '13': WineList("3","Sadie Family Columella","South Africa","Syrah, Mourvèdre","€102"),
    '14': WineList("4","Klein Constantia Vin de Constance","South Africa","Muscat","€84"),
    '15': WineList("5","Meerlust Rubicon","South Africa","Cabernet Sauvignon, Merlot","€37"),
    '16': WineList("6","Boekenhoutskloof Cabernet Sauvignon","South Africa","Cabernet Sauvignon","€74"),
    '17': WineList("7","Eben Sadie Skurfberg","South Africa","Chenin Blanc","€65"),
    '18': WineList("8","De Toren Fusion V","South Africa","Cabernet Sauvignon, Merlot","€46"),
    '19': WineList("9","Warwick Trilogy","South Africa","Cabernet Sauvignon, Merlot, Cabernet Franc","€37"),
    '20': WineList("10","Raats Family Cabernet Franc","South Africa","Cabernet Franc","€46")
}

asian_datastore = {
    '21': WineList("1","Ao Yun","China","Cabernet Sauvignon, Cabernet Franc","€279"),
    '22': WineList("2","Grace Vineyard Chairmans Reserve","China","Cabernet Sauvignon, Merlot","€93"),
    '23': WineList("3","Sula Vineyards Rasa Shiraz","India","Shiraz","€37"),
    '24': WineList("4","Chateau Mercian Koshu Kiiroka","Japan","Koshu","€33"),
    '25': WineList("5","KRSMA Estates Cabernet Sauvignon","India","Cabernet Sauvignon","€46"),
    '26': WineList("6","Grace Vineyard Tasyas Reserve","China","Cabernet Franc","€46"),
    '27': WineList("7","Chateau Musar","Lebanon","Cabernet Sauvignon, Cinsault","€65"),
    '28': WineList("8","Naniwa Winery Koshu","Japan","Koshu","€23"),
    '29': WineList("9","Sapporo Grande Polaire","Japan","Merlot, Cabernet Sauvignon","€37"),
    '30': WineList("10","Helan Qingxue Jia Bei Lan","China","Cabernet Sauvignon","€93")
}

n_american_datastore = {
    '31': WineList("1","Screaming Eagle Cabernet Sauvignon","USA (California)","Cabernet Sauvignon","€3255"),
    '32': WineList("2","Opus One","USA (California)","Cabernet Sauvignon, Merlot","€325"),
    '33': WineList("3","Caymus Special Selection Cabernet Sauvignon","USA (California)","Cabernet Sauvignon","€140"),
    '34': WineList("4","Sine Qua Non Syrah","USA (California)","Syrah","€372"),
    '35': WineList("5","Ridge Monte Bello","USA (California)","Cabernet Sauvignon, Merlot","€232"),
    '36': WineList("6","Mayacamas Cabernet Sauvignon","USA (California)","Cabernet Sauvignon","€140"),
    '37': WineList("7","Domaine Serene Evenstad Reserve Pinot Noir","USA (Oregon)","Pinot Noir","€74"),
    '38': WineList("8","Icewine Inniskillin","Canada","Vidal, Riesling","€56"),
    '39': WineList("9","Monte Xanic Gran Ricardo","Mexico","Cabernet Sauvignon, Merlot, Petit Verdot","€74"),
    '40': WineList("10","Quilceda Creek Cabernet Sauvignon","USA (Washington)","Cabernet Sauvignon","€186")
}

s_american_datastore = {
    '41': WineList("1","Catena Zapata Adrianna Vineyard","Argentina","Malbec","€130"),
    '42': WineList("2","Almaviva","Chile","Cabernet Sauvignon, Carmenère","€112"),
    '43': WineList("3","Clos Apalta","Chile","Carmenère, Merlot, Cabernet Sauvignon","€121"),
    '44': WineList("4","Cheval des Andes","Argentina","Malbec, Cabernet Sauvignon","€93"),
    '45': WineList("5","Achaval Ferrer Finca Bella Vista","Argentina","Malbec","€112"),
    '46': WineList("6","Montes Alpha M","Chile","Cabernet Sauvignon, Merlot","€74"),
    '47': WineList("7","Don Melchor Cabernet Sauvignon","Chile","Cabernet Sauvignon","€112"),
    '48': WineList("8","El Enemigo Gran Enemigo","Argentina","Cabernet Franc","€93"),
    '49': WineList("9","Lapostolle Clos Apalta","Chile","Carmenère, Merlot, Cabernet Sauvignon","€112"),
    '50': WineList("10","Viña Cobos Malbec Marchiori","Argentina","Malbec","€140")
}

australia_datastore = {
    '51': WineList("1","Penfolds Grange","Australia","Shiraz, Cabernet Sauvignon","€651"),
    '52': WineList("2","Henschke Hill of Grace Shiraz","Australia","Shiraz","€605"),
    '53': WineList("3","Cullen Diana Madeline","Australia","Cabernet Sauvignon, Merlot","€121"),
    '54': WineList("4","Cloudy Bay Sauvignon Blanc","New Zealand","Sauvignon Blanc","€32"),
    '55': WineList("5","Torbreck The Laird","Australia","Shiraz","€651"),
    '56': WineList("6","Te Mata Coleraine","New Zealand","Cabernet Sauvignon, Merlot","€84"),
    '57': WineList("7","Ata Rangi Pinot Noir","New Zealand","Pinot Noir","€74"),
    '58': WineList("8","Leeuwin Estate Art Series Chardonnay","Australia","Chardonnay","€93"),
    '59': WineList("9","Vasse Felix Heytesbury Chardonnay","Australia","Chardonnay","€70"),
    '60': WineList("10","Stonyridge Larose","New Zealand","Cabernet Sauvignon, Merlot","€186")
}
