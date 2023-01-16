import ElGamal as el

p=17171810507527611827459888970482558280049759629590793472150559723765848711383835049245937646549939397966259641645103225531930421645608431243042298893897244466652614451421686619053210900424772468013950224816517952238385741132939187922452018984703453411288012329886491758408994179274945133094525718704344872516320174036615158401163102965189811705576881636295731669371188837567695068724031496729629325939591544188700658762744573621881013382784812327126130889653994619368746615568643385510999994642583561480234818951554659200389561319173722050520900128018410903049915827147459638060630603549232119713008292573437433453497

g=16504112626086834307562556557911516801482436189796980917569437678802258423627806531088880182798603958135934374454215115464224501620226427479253834359335927567103141261111369756955806052590791482920380442557084258376180722805195110785020712662517021636062482848271665130841421286183178099472793402104717610977214679807491857436937503954660977499933007331215434060397046183381499506296987451038706150929750626015618873704604170729141396104894631584189750219098304416594911696564839857836438110241542476458957516019484803515042648963320942369364126124313576091775543052858003081488799215856920266461135624985038068743185

h=13373848373727304074099573872186124895161117024560803703177901487562787289757370845910389854469546958123597643116457701586143804625723945169095161154692314666702832132479134348883985791840884424822847882737601768024240458862780435495409688087238094497578702448753271801960397686889078516347068330894832234577133949588283577126698411529224980198563628407117724224985340210273029021686218616427626236030718399898318567447998321086723611910772215661146185899194156398634787110176501068954426328714562457060259031521608426942771568667701832844365311770664034884391530680217866060773799463247572987374602413392645452613640

r=14580602664294001274034633676919139107987868328875858365210024793254972717270097373518264956814973589933955155463165461411853831030877016076206131973924043144201347158167805837391932969457772052471526069681686350096199327827009059266143203785755949549436355719627786929114313049732640144567103119627180304101971994665090794489890193574241345628502628652199408779233388816942828648434257460644626506323604151334383753506018126066682418102617777994406459003384865107538075587771611036550416944875543450064240089041596421259607748082976461301064066032475153360385068064863314804124679983423871349361671859752839124503218

t=2197972781178017162448087755096864423893281135511366947383233515019552485487819668953931225593097251025109297577662745346022041290548338865519391240280077428989987283539048731688312589885841222996426195917602190629041975255270391054887169826613827629997131792031249257443219336078567657442198939766798664067508917665443260370491499590584900913900071729679396892277016877923649319632123379734565631286496085104823047980924930299126319159284697409608679671176571989977647906559552435039733460762948852653149229376885570373881284278928955770440410461633709314225496884902626988287771853109576076808689758788807918785694

# int to bytes array
def intToBytes(pr):
    ln = pr.bit_length()
    bytelen = (ln + 7) // 8
    return pr.to_bytes(bytelen, byteorder="big")

# we know k is between 1 and pow(2,16) - 1
for k in range(1, pow(2,16) - 1):
    # if r = g**k mod(p) (by ElGamal encryption method)
    if r == pow(g,k,p):
        # then plaintext should be equal to = (h**-k) * t 
        ptext = (el.modinv(pow(h, k), p) * t) % p
        print(intToBytes(ptext).decode())
        break