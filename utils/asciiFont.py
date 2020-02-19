

# converts a string to a bitmap with 1p gaps between the chars
def stringToBitMatrix(text):
    out = []
    gap = [[0]] * 8

    for i in text:
        out.append(asciiArr[ord(i)])
        out.append(gap)

    return out


# converts a string to a bitmap with each char extended to 8x8 to occupy exactely one tile
def stringToTileMatrix(text):
    out = []

    for i in text:
        out.append(toTileSize(asciiArr[ord(i)]))

    return out


def toTileSize(char):  # takes a text or char which is then extended to a multiple of 8 from bouth sides with the text in the center
    width = 8 - (len(char[0]) % 8)

    pre = [[0] * int(width / 2)] * 8
    suf = [[0] * (width - len(pre[0]))] * 8

    return concatChars([pre, char, suf])


def stuffBitmap(bitmap, stuffSize):  # stuffes a bitmap from behind to a multiple of stuffSize
    stuffLen = stuffSize - (len(bitmap[0]) % stuffSize)
    stuffArr = [[1] * stuffLen] * 8

    return concatChars([bitmap, stuffArr])


def concatChars(arr):  # concatenates an array of charbitmaps to one large bitmap
    out = [[]] * 8

    for j in arr:
        out = [out[i] + j[i] for i in range(len(out))]

    return out


def printBitmap(char):  # prints the bitmap
    for j in char:
        line = ""
        for i in j:
            if (i == 1):
                line += "█"
            elif (i == 0):
                line += " "

        print(line)


def main():

    myList = concatChars(stringToBitMatrix(" !\"#$%&'()*+,-./0123456789"))
    printBitmap(myList)

# ------------------------------------ CHARS ------------------------------------


empty = [[0] * 8] * 8
unknown = [[1] * 8] * 8

_32 = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]


_33 = [[1],
       [1],
       [1],
       [1],
       [1],
       [1],
       [0],
       [1]]

_34 = [[1, 0, 1],
       [1, 0, 1],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0], ]

_35 = [[0, 0, 0, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 1, 0, 1, 0],
       [0, 0, 0, 0, 0]]

_36 = [[0, 1, 0, 1, 0],
       [0, 1, 1, 1, 1],
       [1, 1, 0, 1, 0],
       [0, 1, 1, 1, 0],
       [0, 1, 1, 1, 0],
       [0, 1, 0, 1, 1],
       [1, 1, 1, 1, 0],
       [0, 1, 0, 1, 0]]

_37 = [[0, 1, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 1, 0]]

_38 = [[0, 1, 1, 0, 0],
       [1, 0, 0, 1, 0],
       [1, 0, 0, 1, 0],
       [0, 1, 1, 0, 0],
       [1, 0, 0, 1, 0],
       [1, 0, 0, 1, 0],
       [1, 0, 1, 1, 0],
       [0, 1, 1, 0, 1]]

_39 = [[1],
       [1],
       [0],
       [0],
       [0],
       [0],
       [0],
       [0]]

_40 = [[0, 0, 1],
       [0, 1, 0],
       [1, 0, 0],
       [1, 0, 0],
       [1, 0, 0],
       [1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]]

_41 = [[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1],
       [0, 0, 1],
       [0, 0, 1],
       [0, 0, 1],
       [0, 1, 0],
       [1, 0, 0]]

_42 = [[1, 0, 1],
       [0, 1, 0],
       [1, 0, 1],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

_43 = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 1, 0],
       [1, 1, 1],
       [0, 1, 0],
       [0, 0, 0],
       [0, 0, 0]]

_44 = [[0, 0],
       [0, 0],
       [0, 0],
       [0, 0],
       [0, 0],
       [0, 0],
       [1, 0],
       [0, 1]]

_45 = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [1, 1, 1],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

_46 = [[0],
       [0],
       [0],
       [0],
       [0],
       [0],
       [0],
       [1]]

_47 = [[0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 1, 0],
       [0, 1, 0, 0],
       [0, 1, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]

_48 = [[0, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 0]]

_49 = [[0, 1],
       [1, 1],
       [0, 1],
       [0, 1],
       [0, 1],
       [0, 1],
       [0, 1],
       [0, 1]]

_50 = [[0, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 1, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 1, 1, 1]]

_51 = [[0, 1, 1, 0],
       [1, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 1, 1],
       [0, 0, 1, 1],
       [0, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 0]]

_52 = [[0, 0, 1, 0],
       [0, 0, 1, 0],
       [0, 1, 0, 0],
       [0, 1, 0, 0],
       [1, 0, 1, 0],
       [1, 1, 1, 1],
       [0, 0, 1, 0],
       [0, 0, 1, 0]]

_53 = [[1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       [1, 1, 1, 0]]

_54 = [[0, 0, 1, 1],
       [0, 1, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 0]]

_55 = [[1, 1, 1, 1],
       [0, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 1, 0],
       [0, 1, 0, 0],
       [0, 1, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]

_56 = [[0, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 0]]

_57 = [[0, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 1],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 1, 0],
       [1, 1, 0, 0]]

_58 = [[0],
       [0],
       [0],
       [1],
       [0],
       [0],
       [1],
       [0]]

_59 = [[0, 0],
       [0, 0],
       [0, 0],
       [1, 0],
       [0, 0],
       [0, 0],
       [1, 0],
       [0, 1]]

_60 = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 1, 1, 0],
       [1, 0, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 1],
       [0, 0, 0, 0]]

_61 = None
_62 = None
_63 = None
_64 = None
_65 = None
_66 = None
_67 = None
_68 = None
_69 = None
_70 = None
_71 = None
_72 = None
_73 = None
_74 = None
_75 = None
_76 = None
_77 = None
_78 = None
_79 = None
_80 = None
_81 = None
_82 = None
_83 = None
_84 = None
_85 = None
_86 = None
_87 = None
_88 = None
_89 = None
_90 = None
_91 = None
_92 = None
_93 = None
_94 = None
_95 = None
_96 = None
_97 = None
_98 = None
_99 = None
_100 = None
_101 = None
_102 = None
_103 = None
_104 = None
_105 = None
_106 = None
_107 = None
_108 = None
_109 = None
_110 = None
_111 = None
_112 = None
_113 = None
_114 = None
_115 = None
_116 = None
_117 = None
_118 = None
_119 = None
_120 = None
_121 = None
_122 = None
_123 = None
_124 = None
_125 = None
_126 = None

asciiArr = [unknown, unknown, unknown, unknown, unknown, unknown, unknown, unknown,
            unknown, unknown, unknown, unknown, unknown, unknown, unknown, unknown,
            unknown, unknown, unknown, unknown, unknown, unknown, unknown, unknown,
            unknown, unknown, unknown, unknown, unknown, unknown, unknown, unknown,
            _32, _33, _34, _35, _36, _37, _38, _39,
            _40, _41, _42, _43, _44, _45, _46, _47,
            _48, _49, _50, _51, _52, _53, _54, _55,
            _56, _57, _58, _59, _60, _61, _62, _63,
            _64, _65, _66, _67, _68, _69, _70, _71,
            _72, _73, _74, _75, _76, _77, _78, _79,
            _80, _81, _82, _83, _84, _85, _86, _87,
            _88, _89, _90, _91, _92, _93, _94, _95,
            _96, _97, _98, _99, _100, _101, _102, _103,
            _104, _105, _106, _107, _108, _109, _110, _111,
            _112, _113, _114, _115, _116, _117, _118, _119,
            _120, _121, _122, _123, _124, _125, _126, unknown]

if __name__ == "__main__":
    main()
