%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-o
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1369:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mflogo.tar.xz
Source1370:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mflogo.doc.tar.xz
Source1406:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mfnfss.tar.xz
Source1407:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mfnfss.doc.tar.xz
Source1484:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/margbib.tar.xz
Source1485:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/margbib.doc.tar.xz
Source1670:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/manfnt-font.tar.xz
Source1671:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mflogo-font.tar.xz
Source1672:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mflogo-font.doc.tar.xz
Source1952:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathabx.tar.xz
Source1953:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathabx.doc.tar.xz
Source1954:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathabx-type1.tar.xz
Source1955:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathabx-type1.doc.tar.xz
Source1956:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathdesign.tar.xz
Source1957:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathdesign.doc.tar.xz
Source1958:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mdputu.tar.xz
Source1959:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mdputu.doc.tar.xz
Source1960:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mdsymbol.tar.xz
Source1961:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mdsymbol.doc.tar.xz
Source1963:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/merriweather.tar.xz
Source1964:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/merriweather.doc.tar.xz
Source1965:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mintspirit.tar.xz
Source1966:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mintspirit.doc.tar.xz
Source1967:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mnsymbol.tar.xz
Source1968:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mnsymbol.doc.tar.xz
Source2132:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/marvosym.tar.xz
Source2133:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/marvosym.doc.tar.xz
Source2135:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathpazo.tar.xz
Source2136:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathpazo.doc.tar.xz
Source2305:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathdots.tar.xz
Source2306:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathdots.doc.tar.xz
Source2308:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metatex.tar.xz
Source2309:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metatex.doc.tar.xz
Source2310:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/midnight.tar.xz
Source2311:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/midnight.doc.tar.xz
Source2428:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metrix.tar.xz
Source2429:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metrix.doc.tar.xz
Source2639:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/macros2e.doc.tar.xz
Source2640:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/math-e.doc.tar.xz
Source2641:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/maths-symbols.doc.tar.xz
Source2642:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/memdesign.doc.tar.xz
Source2643:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metafont-beginners.doc.tar.xz
Source2644:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metapost-examples.doc.tar.xz
Source2726:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mafr.tar.xz
Source2727:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mafr.doc.tar.xz
Source2773:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/microtype-de.doc.tar.xz
Source2920:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/memoir.tar.xz
Source2921:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/memoir.doc.tar.xz
Source3050:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathtools.tar.xz
Source3051:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathtools.doc.tar.xz
Source3053:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mdwtools.tar.xz
Source3054:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mdwtools.doc.tar.xz
Source3056:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metalogo.tar.xz
Source3057:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metalogo.doc.tar.xz
Source3059:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/microtype.tar.xz
Source3060:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/microtype.doc.tar.xz
Source3199:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makeshape.tar.xz
Source3200:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makeshape.doc.tar.xz
Source3204:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/miniplot.tar.xz
Source3205:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/miniplot.doc.tar.xz
Source4520:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/macroswap.tar.xz
Source4521:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/macroswap.doc.tar.xz
Source4523:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/magaz.tar.xz
Source4524:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/magaz.doc.tar.xz
Source4525:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mailing.tar.xz
Source4526:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mailing.doc.tar.xz
Source4528:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mailmerge.tar.xz
Source4529:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mailmerge.doc.tar.xz
Source4531:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makebarcode.tar.xz
Source4532:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makebarcode.doc.tar.xz
Source4533:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makebox.tar.xz
Source4534:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makebox.doc.tar.xz
Source4536:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makecell.tar.xz
Source4537:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makecell.doc.tar.xz
Source4539:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makecirc.tar.xz
Source4540:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makecirc.doc.tar.xz
Source4541:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makecmds.tar.xz
Source4542:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makecmds.doc.tar.xz
Source4547:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makeglos.tar.xz
Source4548:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makeglos.doc.tar.xz
Source4549:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mandi.tar.xz
Source4550:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mandi.doc.tar.xz
Source4552:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/manfnt.tar.xz
Source4554:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/manuscript.tar.xz
Source4555:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/manuscript.doc.tar.xz
Source4557:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/marginfix.tar.xz
Source4558:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/marginfix.doc.tar.xz
Source4560:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/marginnote.tar.xz
Source4561:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/marginnote.doc.tar.xz
Source4563:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathalfa.tar.xz
Source4564:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathalfa.doc.tar.xz
Source4565:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathastext.tar.xz
Source4566:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathastext.doc.tar.xz
Source4568:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathexam.tar.xz
Source4569:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathexam.doc.tar.xz
Source4571:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/maybemath.tar.xz
Source4572:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/maybemath.doc.tar.xz
Source4573:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mbenotes.tar.xz
Source4574:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mbenotes.doc.tar.xz
Source4575:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mcaption.tar.xz
Source4576:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mcaption.doc.tar.xz
Source4578:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mceinleger.tar.xz
Source4579:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mceinleger.doc.tar.xz
Source4580:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mcite.tar.xz
Source4581:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mcite.doc.tar.xz
Source4583:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mciteplus.tar.xz
Source4584:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mciteplus.doc.tar.xz
Source4585:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mdframed.tar.xz
Source4586:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mdframed.doc.tar.xz
Source4588:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/media9.tar.xz
Source4589:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/media9.doc.tar.xz
Source4591:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/medstarbeamer.tar.xz
Source4592:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/medstarbeamer.doc.tar.xz
Source4593:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/meetingmins.tar.xz
Source4594:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/meetingmins.doc.tar.xz
Source4596:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/memexsupp.tar.xz
Source4597:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/memexsupp.doc.tar.xz
Source4598:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/memory.tar.xz
Source4599:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/memory.doc.tar.xz
Source4601:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/menu.tar.xz
Source4602:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/menu.doc.tar.xz
Source4604:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/menukeys.tar.xz
Source4605:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/menukeys.doc.tar.xz
Source4607:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/method.tar.xz
Source4608:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/method.doc.tar.xz
Source4610:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metre.tar.xz
Source4611:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metre.doc.tar.xz
Source4613:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mfirstuc.tar.xz
Source4614:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mfirstuc.doc.tar.xz
Source4616:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mftinc.tar.xz
Source4617:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mftinc.doc.tar.xz
Source4619:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/midpage.tar.xz
Source4620:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/midpage.doc.tar.xz
Source4621:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minibox.tar.xz
Source4622:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minibox.doc.tar.xz
Source4624:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minifp.tar.xz
Source4625:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minifp.doc.tar.xz
Source4627:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minipage-marginpar.tar.xz
Source4628:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minipage-marginpar.doc.tar.xz
Source4630:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minitoc.tar.xz
Source4631:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minitoc.doc.tar.xz
Source4632:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minorrevision.tar.xz
Source4633:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minorrevision.doc.tar.xz
Source4634:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minted.tar.xz
Source4635:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minted.doc.tar.xz
Source4637:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minutes.tar.xz
Source4638:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minutes.doc.tar.xz
Source4640:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mla-paper.tar.xz
Source4641:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mla-paper.doc.tar.xz
Source4642:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mlist.tar.xz
Source4643:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mlist.doc.tar.xz
Source4645:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mmap.tar.xz
Source4646:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mmap.doc.tar.xz
Source4647:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mnotes.tar.xz
Source4648:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mnotes.doc.tar.xz
Source5865:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathcomp.tar.xz
Source5866:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathcomp.doc.tar.xz
Source5868:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mattens.tar.xz
Source5869:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mattens.doc.tar.xz
Source5871:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mhequ.tar.xz
Source5872:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mhequ.doc.tar.xz
Source5975:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mcf2graph.tar.xz
Source5976:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mcf2graph.doc.tar.xz
Source5977:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metago.tar.xz
Source5978:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metago.doc.tar.xz
Source5979:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metaobj.tar.xz
Source5980:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metaobj.doc.tar.xz
Source5981:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metaplot.tar.xz
Source5982:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metaplot.doc.tar.xz
Source5983:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metauml.tar.xz
Source5984:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metauml.doc.tar.xz
Source5985:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mfpic.tar.xz
Source5986:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mfpic.doc.tar.xz
Source5988:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mfpic4ode.tar.xz
Source5989:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mfpic4ode.doc.tar.xz
Source6095:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mkpattern.tar.xz
Source6096:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mkpattern.doc.tar.xz
Source6121:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makeplot.tar.xz
Source6122:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makeplot.doc.tar.xz
Source6428:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/matc3.tar.xz
Source6429:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/matc3.doc.tar.xz
Source6431:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/matc3mem.tar.xz
Source6432:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/matc3mem.doc.tar.xz
Source6434:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mcmthesis.tar.xz
Source6435:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mcmthesis.doc.tar.xz
Source6437:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mentis.tar.xz
Source6438:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mentis.doc.tar.xz
Source6440:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mnras.tar.xz
Source6441:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mnras.doc.tar.xz
Source6692:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/matlab-prettifier.tar.xz
Source6693:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/matlab-prettifier.doc.tar.xz
Source6695:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mhchem.tar.xz
Source6696:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mhchem.doc.tar.xz
Source6697:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/miller.tar.xz
Source6698:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/miller.doc.tar.xz
Source6760:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathspec.tar.xz
Source6761:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathspec.doc.tar.xz
Source7425:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makebase.tar.xz
Source7426:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makebase.doc.tar.xz
Source7428:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/markdown.tar.xz
Source7429:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/markdown.doc.tar.xz
Source7431:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathpartir.tar.xz
Source7432:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathpartir.doc.tar.xz
Source7437:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/miama.tar.xz
Source7438:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/miama.doc.tar.xz
Source7842:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/maker.tar.xz
Source7843:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/maker.doc.tar.xz
Source7844:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/marginfit.tar.xz
Source7845:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/marginfit.doc.tar.xz
Source7846:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/math-into-latex-4.doc.tar.xz
Source7847:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mcexam.tar.xz
Source7848:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mcexam.doc.tar.xz
Source7849:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mendex-doc.doc.tar.xz
Source7850:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/milog.tar.xz
Source7851:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/milog.doc.tar.xz
Source7852:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/missaali.tar.xz
Source7853:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/missaali.doc.tar.xz
Source8052:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mensa-tex.tar.xz
Source8053:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mensa-tex.doc.tar.xz
Source8210:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/manyind.tar.xz
Source8211:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/manyind.doc.tar.xz
Source8212:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathfam256.tar.xz
Source8213:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathfam256.doc.tar.xz
Source8214:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathfixs.tar.xz
Source8215:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathfixs.doc.tar.xz
Source8216:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathfont.tar.xz
Source8217:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathfont.doc.tar.xz
Source8218:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathpunctspace.tar.xz
Source8219:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathpunctspace.doc.tar.xz
Source8222:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mgltex.tar.xz
Source8223:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mgltex.doc.tar.xz
Source8224:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/milsymb.tar.xz
Source8225:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/milsymb.doc.tar.xz
Source8226:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minidocument.tar.xz
Source8227:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/minidocument.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-mflogo
Provides:       tex-mflogo = %{tl_version}
License:        LPPL
Summary:        LaTeX support for Metafont logo fonts
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(mflogo.sty) = %{tl_version}, tex(ulogo.fd) = %{tl_version}

%description -n texlive-mflogo
LaTeX package and font definition file to access the Knuthian
mflogo fonts described in 'The Metafontbook' and to typeset
Metafont logos in LaTeX documents.

%package -n texlive-mflogo-doc
Summary:        Documentation for mflogo
Version:        svn42428
Provides:       tex-mflogo-doc
AutoReqProv:    No

%description -n texlive-mflogo-doc
Documentation for mflogo

%package -n texlive-mfnfss
Provides:       tex-mfnfss = %{tl_version}
License:        LPPL
Summary:        Packages to typeset oldgerman and pandora fonts in LaTeX
Version:        svn46036
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(oldgerm.sty) = %{tl_version}, tex(ot1panr.fd) = %{tl_version}
Provides:       tex(ot1pss.fd) = %{tl_version}, tex(pandora.sty) = %{tl_version}
Provides:       tex(uyfrak.fd) = %{tl_version}, tex(uygoth.fd) = %{tl_version}
Provides:       tex(uyinit.fd) = %{tl_version}, tex(uyswab.fd) = %{tl_version}

%description -n texlive-mfnfss
This bundle contains two packages: - oldgerm, a package to
typeset with old german fonts designed by Yannis Haralambous. -
pandora, a package to typeset with Pandora fonts designed by
Neena Billawala. Note that support for the Pandora fonts is
also available via the pandora-latex package.

%package -n texlive-mfnfss-doc
Summary:        Documentation for mfnfss
Version:        svn46036
Provides:       tex-mfnfss-doc
AutoReqProv:    No

%description -n texlive-mfnfss-doc
Documentation for mfnfss

%package -n texlive-margbib
Provides:       tex-margbib = %{tl_version}
License:        GPL+
Summary:        Display bibitem tags in the margins
Version:        svn15878.1.0c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(margbib.sty) = %{tl_version}

%description -n texlive-margbib
The package redefines the 'thebibliography' environment to
place the citation key into the margin.

%package -n texlive-margbib-doc
Summary:        Documentation for margbib
Version:        svn15878.1.0c

Provides:       tex-margbib-doc
AutoReqProv:    No

%description -n texlive-margbib-doc
Documentation for margbib

%package -n texlive-manfnt-font
Provides:       tex-manfnt-font = %{tl_version}
License:        LPPL
Summary:        manfnt-font package
Version:        svn45777
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(manfnt.map) = %{tl_version}, tex(manfnt.pfb) = %{tl_version}

%description -n texlive-manfnt-font
manfnt-font package

%package -n texlive-mflogo-font
Provides:       tex-mflogo-font = %{tl_version}
License:        Knuth
Summary:        Metafont logo font
Version:        svn36898.1.002

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(mflogo.map) = %{tl_version}, tex(logo10.pfb) = %{tl_version}
Provides:       tex(logo8.pfb) = %{tl_version}, tex(logo9.pfb) = %{tl_version}
Provides:       tex(logobf10.pfb) = %{tl_version}, tex(logod10.pfb) = %{tl_version}
Provides:       tex(logosl10.pfb) = %{tl_version}, tex(logosl8.pfb) = %{tl_version}
Provides:       tex(logosl9.pfb) = %{tl_version}

%description -n texlive-mflogo-font
These fonts were created in Metafont by Knuth, for his own
publications. At some stage, the letters 'P' and 'S' were
added, so that the MetaPost logo could also be expressed. The
fonts were originally issued (of course) as Metafont source;
they have since been autotraced and reissued in Adobe Type 1
format by Taco Hoekwater.

%package -n texlive-mflogo-font-doc
Summary:        Documentation for mflogo-font
Version:        svn36898.1.002

Provides:       tex-mflogo-font-doc
AutoReqProv:    No

%description -n texlive-mflogo-font-doc
Documentation for mflogo-font

%package -n texlive-mathabx
Provides:       tex-mathabx = %{tl_version}
License:        LPPL
Summary:        Three series of mathematical symbols
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(matha10.tfm) = %{tl_version}, tex(matha12.tfm) = %{tl_version}
Provides:       tex(matha5.tfm) = %{tl_version}, tex(matha6.tfm) = %{tl_version}
Provides:       tex(matha7.tfm) = %{tl_version}, tex(matha8.tfm) = %{tl_version}
Provides:       tex(matha9.tfm) = %{tl_version}, tex(mathastrotest10.tfm) = %{tl_version}
Provides:       tex(mathb10.tfm) = %{tl_version}, tex(mathb12.tfm) = %{tl_version}
Provides:       tex(mathb5.tfm) = %{tl_version}, tex(mathb6.tfm) = %{tl_version}
Provides:       tex(mathb7.tfm) = %{tl_version}, tex(mathb8.tfm) = %{tl_version}
Provides:       tex(mathb9.tfm) = %{tl_version}, tex(mathc10.tfm) = %{tl_version}
Provides:       tex(mathu10.tfm) = %{tl_version}, tex(mathux10.tfm) = %{tl_version}
Provides:       tex(mathx10.tfm) = %{tl_version}, tex(mathx12.tfm) = %{tl_version}
Provides:       tex(mathx5.tfm) = %{tl_version}, tex(mathx6.tfm) = %{tl_version}
Provides:       tex(mathx7.tfm) = %{tl_version}, tex(mathx8.tfm) = %{tl_version}
Provides:       tex(mathx9.tfm) = %{tl_version}, tex(mathabx.sty) = %{tl_version}
Provides:       tex(mathabx.tex) = %{tl_version}

%description -n texlive-mathabx
Mathabx is a set of 3 mathematical symbols font series: matha,
mathb and mathx. They are defined by Metafont code and should
be of reasonable quality (bitmap output). Things change from
time to time, so there is no claim of stability (encoding,
metrics, design). The package includes Plain TeX and LaTeX
support macros. A version of the fonts, in Adobe Type 1 format,
is also available.

%package -n texlive-mathabx-doc
Summary:        Documentation for mathabx
Version:        svn15878.0

Provides:       tex-mathabx-doc
AutoReqProv:    No

%description -n texlive-mathabx-doc
Documentation for mathabx

%package -n texlive-mathabx-type1
Provides:       tex-mathabx-type1 = %{tl_version}
License:        LPPL
Summary:        Outline version of the mathabx fonts
Version:        svn21129.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex-mathabx
Provides:       tex(mathabx.map) = %{tl_version}, tex(matha10.pfb) = %{tl_version}
Provides:       tex(matha12.pfb) = %{tl_version}, tex(matha5.pfb) = %{tl_version}
Provides:       tex(matha6.pfb) = %{tl_version}, tex(matha7.pfb) = %{tl_version}
Provides:       tex(matha8.pfb) = %{tl_version}, tex(matha9.pfb) = %{tl_version}
Provides:       tex(mathastrotest10.pfb) = %{tl_version}
Provides:       tex(mathb10.pfb) = %{tl_version}, tex(mathb12.pfb) = %{tl_version}
Provides:       tex(mathb5.pfb) = %{tl_version}, tex(mathb6.pfb) = %{tl_version}
Provides:       tex(mathb7.pfb) = %{tl_version}, tex(mathb8.pfb) = %{tl_version}
Provides:       tex(mathb9.pfb) = %{tl_version}, tex(mathc10.pfb) = %{tl_version}
Provides:       tex(mathu10.pfb) = %{tl_version}, tex(mathux10.pfb) = %{tl_version}
Provides:       tex(mathx10.pfb) = %{tl_version}, tex(mathx12.pfb) = %{tl_version}
Provides:       tex(mathx5.pfb) = %{tl_version}, tex(mathx6.pfb) = %{tl_version}
Provides:       tex(mathx7.pfb) = %{tl_version}, tex(mathx8.pfb) = %{tl_version}
Provides:       tex(mathx9.pfb) = %{tl_version}

%description -n texlive-mathabx-type1
This is an Adobe Type 1 outline version of the mathabx fonts.

%package -n texlive-mathabx-type1-doc
Summary:        Documentation for mathabx-type1
Version:        svn21129.0

Provides:       tex-mathabx-type1-doc
AutoReqProv:    No
Requires:       tex-mathabx-doc

%description -n texlive-mathabx-type1-doc
Documentation for mathabx-type1

%package -n texlive-mathdesign
Provides:       tex-mathdesign = %{tl_version}
License:        GPL+
Summary:        Mathematical fonts to fit with particular text fonts
Version:        svn31639.2.31

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(keyval.sty), tex(ifthen.sty), tex(fontenc.sty), tex(xkeyval.sty)
Requires:       tex(texnansi.enc)
Provides:       tex(a_2dncez.enc) = %{tl_version}, tex(a_2rwgaw.enc) = %{tl_version}
Provides:       tex(a_42s2zl.enc) = %{tl_version}, tex(a_45o73x.enc) = %{tl_version}
Provides:       tex(a_4b5i6w.enc) = %{tl_version}, tex(a_57soyv.enc) = %{tl_version}
Provides:       tex(a_csqf63.enc) = %{tl_version}, tex(a_e65dz6.enc) = %{tl_version}
Provides:       tex(a_g2masa.enc) = %{tl_version}, tex(a_g47ck7.enc) = %{tl_version}
Provides:       tex(a_ipzj2o.enc) = %{tl_version}, tex(a_kld4uc.enc) = %{tl_version}
Provides:       tex(a_mdpn2k.enc) = %{tl_version}, tex(a_n2elaj.enc) = %{tl_version}
Provides:       tex(a_oxfbe4.enc) = %{tl_version}, tex(a_py5znv.enc) = %{tl_version}
Provides:       tex(a_qnfjtt.enc) = %{tl_version}, tex(a_qzg4u4.enc) = %{tl_version}
Provides:       tex(a_r2nxhw.enc) = %{tl_version}, tex(a_rl4tn2.enc) = %{tl_version}
Provides:       tex(a_rxz3ga.enc) = %{tl_version}, tex(a_telfo7.enc) = %{tl_version}
Provides:       tex(a_uwwzqd.enc) = %{tl_version}, tex(a_yezm6g.enc) = %{tl_version}
Provides:       tex(md8x.enc) = %{tl_version}, tex(mdbch.map) = %{tl_version}
Provides:       tex(mdgreek.map) = %{tl_version}, tex(mdici.map) = %{tl_version}
Provides:       tex(mdpgd.map) = %{tl_version}, tex(mdpus.map) = %{tl_version}
Provides:       tex(mdput.map) = %{tl_version}, tex(mdugm.map) = %{tl_version}
Provides:       tex(bchb8a.tfm) = %{tl_version}, tex(bchbc8a.tfm) = %{tl_version}
Provides:       tex(bchbc8y.tfm) = %{tl_version}, tex(bchbi8a.tfm) = %{tl_version}
Provides:       tex(bchr8a.tfm) = %{tl_version}, tex(bchrc8a.tfm) = %{tl_version}
Provides:       tex(bchrc8y.tfm) = %{tl_version}, tex(bchri8a.tfm) = %{tl_version}
Provides:       tex(md-chb7m.tfm) = %{tl_version}, tex(md-chb7t.tfm) = %{tl_version}
Provides:       tex(md-chb7v.tfm) = %{tl_version}, tex(md-chb7y.tfm) = %{tl_version}
Provides:       tex(md-chb8c.tfm) = %{tl_version}, tex(md-chb8t.tfm) = %{tl_version}
Provides:       tex(md-chb8y.tfm) = %{tl_version}, tex(md-chbc8y.tfm) = %{tl_version}
Provides:       tex(md-chbi7m.tfm) = %{tl_version}, tex(md-chbi7t.tfm) = %{tl_version}
Provides:       tex(md-chbi8c.tfm) = %{tl_version}, tex(md-chbi8t.tfm) = %{tl_version}
Provides:       tex(md-chbi8y.tfm) = %{tl_version}, tex(md-chbma.tfm) = %{tl_version}
Provides:       tex(md-chbmb.tfm) = %{tl_version}, tex(md-chbo7t.tfm) = %{tl_version}
Provides:       tex(md-chbo8c.tfm) = %{tl_version}, tex(md-chbo8t.tfm) = %{tl_version}
Provides:       tex(md-chbo8y.tfm) = %{tl_version}, tex(md-chboc8y.tfm) = %{tl_version}
Provides:       tex(md-chr7m.tfm) = %{tl_version}, tex(md-chr7t.tfm) = %{tl_version}
Provides:       tex(md-chr7v.tfm) = %{tl_version}, tex(md-chr7y.tfm) = %{tl_version}
Provides:       tex(md-chr8c.tfm) = %{tl_version}, tex(md-chr8t.tfm) = %{tl_version}
Provides:       tex(md-chr8y.tfm) = %{tl_version}, tex(md-chrc8y.tfm) = %{tl_version}
Provides:       tex(md-chree.tfm) = %{tl_version}, tex(md-chri7m.tfm) = %{tl_version}
Provides:       tex(md-chri7t.tfm) = %{tl_version}, tex(md-chri8c.tfm) = %{tl_version}
Provides:       tex(md-chri8t.tfm) = %{tl_version}, tex(md-chri8y.tfm) = %{tl_version}
Provides:       tex(md-chrma.tfm) = %{tl_version}, tex(md-chrmb.tfm) = %{tl_version}
Provides:       tex(md-chro7t.tfm) = %{tl_version}, tex(md-chro8c.tfm) = %{tl_version}
Provides:       tex(md-chro8t.tfm) = %{tl_version}, tex(md-chro8y.tfm) = %{tl_version}
Provides:       tex(md-chroc8y.tfm) = %{tl_version}, tex(mdbchb7m.tfm) = %{tl_version}
Provides:       tex(mdbchb7t.tfm) = %{tl_version}, tex(mdbchb7v.tfm) = %{tl_version}
Provides:       tex(mdbchb7y.tfm) = %{tl_version}, tex(mdbchb8c.tfm) = %{tl_version}
Provides:       tex(mdbchb8t.tfm) = %{tl_version}, tex(mdbchbc8t.tfm) = %{tl_version}
Provides:       tex(mdbchbfc8t.tfm) = %{tl_version}, tex(mdbchbi7m.tfm) = %{tl_version}
Provides:       tex(mdbchbi7t.tfm) = %{tl_version}, tex(mdbchbi8c.tfm) = %{tl_version}
Provides:       tex(mdbchbi8t.tfm) = %{tl_version}, tex(mdbchbifc8t.tfm) = %{tl_version}
Provides:       tex(mdbchbma.tfm) = %{tl_version}, tex(mdbchbmb.tfm) = %{tl_version}
Provides:       tex(mdbchbo7t.tfm) = %{tl_version}, tex(mdbchbo8c.tfm) = %{tl_version}
Provides:       tex(mdbchbo8t.tfm) = %{tl_version}, tex(mdbchbofc8t.tfm) = %{tl_version}
Provides:       tex(mdbchr7m.tfm) = %{tl_version}, tex(mdbchr7t.tfm) = %{tl_version}
Provides:       tex(mdbchr7v.tfm) = %{tl_version}, tex(mdbchr7y.tfm) = %{tl_version}
Provides:       tex(mdbchr8c.tfm) = %{tl_version}, tex(mdbchr8t.tfm) = %{tl_version}
Provides:       tex(mdbchrc8t.tfm) = %{tl_version}, tex(mdbchrfc8t.tfm) = %{tl_version}
Provides:       tex(mdbchri7m.tfm) = %{tl_version}, tex(mdbchri7t.tfm) = %{tl_version}
Provides:       tex(mdbchri8c.tfm) = %{tl_version}, tex(mdbchri8t.tfm) = %{tl_version}
Provides:       tex(mdbchrifc8t.tfm) = %{tl_version}, tex(mdbchrma.tfm) = %{tl_version}
Provides:       tex(mdbchrmb.tfm) = %{tl_version}, tex(mdbchro7t.tfm) = %{tl_version}
Provides:       tex(mdbchro8c.tfm) = %{tl_version}, tex(mdbchro8t.tfm) = %{tl_version}
Provides:       tex(mdbchrofc8t.tfm) = %{tl_version}, tex(md-grbb7m.tfm) = %{tl_version}
Provides:       tex(md-grbbi7m.tfm) = %{tl_version}, tex(md-grbr7m.tfm) = %{tl_version}
Provides:       tex(md-grbri7m.tfm) = %{tl_version}, tex(md-grdb7m.tfm) = %{tl_version}
Provides:       tex(md-grdbi7m.tfm) = %{tl_version}, tex(md-grdr7m.tfm) = %{tl_version}
Provides:       tex(md-grdri7m.tfm) = %{tl_version}, tex(mdgrbCb7m.tfm) = %{tl_version}
Provides:       tex(mdgrbCbi7m.tfm) = %{tl_version}, tex(mdgrbCr7m.tfm) = %{tl_version}
Provides:       tex(mdgrbCri7m.tfm) = %{tl_version}, tex(mdgrbb7m.tfm) = %{tl_version}
Provides:       tex(mdgrbbi7m.tfm) = %{tl_version}, tex(mdgrbr7m.tfm) = %{tl_version}
Provides:       tex(mdgrbri7m.tfm) = %{tl_version}, tex(mdgrdCb7m.tfm) = %{tl_version}
Provides:       tex(mdgrdCbi7m.tfm) = %{tl_version}, tex(mdgrdCri7m.tfm) = %{tl_version}
Provides:       tex(mdgrdb7m.tfm) = %{tl_version}, tex(mdgrdbi7m.tfm) = %{tl_version}
Provides:       tex(mdgrdr7m.tfm) = %{tl_version}, tex(mdgrdrC7m.tfm) = %{tl_version}
Provides:       tex(mdgrdri7m.tfm) = %{tl_version}, tex(md-cib7m.tfm) = %{tl_version}
Provides:       tex(md-cib7t.tfm) = %{tl_version}, tex(md-cib7v.tfm) = %{tl_version}
Provides:       tex(md-cib7y.tfm) = %{tl_version}, tex(md-cib8c.tfm) = %{tl_version}
Provides:       tex(md-cib8t.tfm) = %{tl_version}, tex(md-cibee.tfm) = %{tl_version}
Provides:       tex(md-cibi7m.tfm) = %{tl_version}, tex(md-cibi7t.tfm) = %{tl_version}
Provides:       tex(md-cibi8c.tfm) = %{tl_version}, tex(md-cibi8t.tfm) = %{tl_version}
Provides:       tex(md-cibma.tfm) = %{tl_version}, tex(md-cibmb.tfm) = %{tl_version}
Provides:       tex(md-cir7m.tfm) = %{tl_version}, tex(md-cir7t.tfm) = %{tl_version}
Provides:       tex(md-cir7v.tfm) = %{tl_version}, tex(md-cir7y.tfm) = %{tl_version}
Provides:       tex(md-cir8c.tfm) = %{tl_version}, tex(md-cir8t.tfm) = %{tl_version}
Provides:       tex(md-ciree.tfm) = %{tl_version}, tex(md-ciri7m.tfm) = %{tl_version}
Provides:       tex(md-ciri7t.tfm) = %{tl_version}, tex(md-ciri8c.tfm) = %{tl_version}
Provides:       tex(md-ciri8t.tfm) = %{tl_version}, tex(md-cirma.tfm) = %{tl_version}
Provides:       tex(md-cirmb.tfm) = %{tl_version}, tex(mdicib7m.tfm) = %{tl_version}
Provides:       tex(mdicib7t.tfm) = %{tl_version}, tex(mdicib7v.tfm) = %{tl_version}
Provides:       tex(mdicib7y.tfm) = %{tl_version}, tex(mdicib8c.tfm) = %{tl_version}
Provides:       tex(mdicib8t.tfm) = %{tl_version}, tex(mdicibc8c.tfm) = %{tl_version}
Provides:       tex(mdicibc8t.tfm) = %{tl_version}, tex(mdicibfc8t.tfm) = %{tl_version}
Provides:       tex(mdicibi7m.tfm) = %{tl_version}, tex(mdicibi7t.tfm) = %{tl_version}
Provides:       tex(mdicibi8c.tfm) = %{tl_version}, tex(mdicibi8t.tfm) = %{tl_version}
Provides:       tex(mdicibic8c.tfm) = %{tl_version}, tex(mdicibic8t.tfm) = %{tl_version}
Provides:       tex(mdicibifc8t.tfm) = %{tl_version}, tex(mdicibma.tfm) = %{tl_version}
Provides:       tex(mdicibmb.tfm) = %{tl_version}, tex(mdicic8c.tfm) = %{tl_version}
Provides:       tex(mdicic8t.tfm) = %{tl_version}, tex(mdicicc8c.tfm) = %{tl_version}
Provides:       tex(mdicicc8t.tfm) = %{tl_version}, tex(mdicicfc8t.tfm) = %{tl_version}
Provides:       tex(mdicici8c.tfm) = %{tl_version}, tex(mdicici8t.tfm) = %{tl_version}
Provides:       tex(mdicicic8c.tfm) = %{tl_version}, tex(mdicicic8t.tfm) = %{tl_version}
Provides:       tex(mdicicifc8t.tfm) = %{tl_version}, tex(mdicir7m.tfm) = %{tl_version}
Provides:       tex(mdicir7t.tfm) = %{tl_version}, tex(mdicir7v.tfm) = %{tl_version}
Provides:       tex(mdicir7y.tfm) = %{tl_version}, tex(mdicir8c.tfm) = %{tl_version}
Provides:       tex(mdicir8t.tfm) = %{tl_version}, tex(mdicirc8c.tfm) = %{tl_version}
Provides:       tex(mdicirc8t.tfm) = %{tl_version}, tex(mdicirfc8t.tfm) = %{tl_version}
Provides:       tex(mdiciri7m.tfm) = %{tl_version}, tex(mdiciri7t.tfm) = %{tl_version}
Provides:       tex(mdiciri8c.tfm) = %{tl_version}, tex(mdiciri8t.tfm) = %{tl_version}
Provides:       tex(mdiciric8c.tfm) = %{tl_version}, tex(mdiciric8t.tfm) = %{tl_version}
Provides:       tex(mdicirifc8t.tfm) = %{tl_version}, tex(mdicirma.tfm) = %{tl_version}
Provides:       tex(mdicirmb.tfm) = %{tl_version}, tex(mdwcib7m.tfm) = %{tl_version}
Provides:       tex(mdwcib7y.tfm) = %{tl_version}, tex(mdwcib8t.tfm) = %{tl_version}
Provides:       tex(mdwcibc8t.tfm) = %{tl_version}, tex(mdwcibi7m.tfm) = %{tl_version}
Provides:       tex(mdwcibi7y.tfm) = %{tl_version}, tex(mdwcibi8t.tfm) = %{tl_version}
Provides:       tex(mdwcibic8t.tfm) = %{tl_version}, tex(mdwcic7m.tfm) = %{tl_version}
Provides:       tex(mdwcic7y.tfm) = %{tl_version}, tex(mdwcic8t.tfm) = %{tl_version}
Provides:       tex(mdwcicc8t.tfm) = %{tl_version}, tex(mdwcici7m.tfm) = %{tl_version}
Provides:       tex(mdwcici7y.tfm) = %{tl_version}, tex(mdwcici8t.tfm) = %{tl_version}
Provides:       tex(mdwcicic8t.tfm) = %{tl_version}, tex(mdwcir7m.tfm) = %{tl_version}
Provides:       tex(mdwcir7y.tfm) = %{tl_version}, tex(mdwcir8t.tfm) = %{tl_version}
Provides:       tex(mdwcirc8t.tfm) = %{tl_version}, tex(mdwciri7m.tfm) = %{tl_version}
Provides:       tex(mdwciri7y.tfm) = %{tl_version}, tex(mdwciri8t.tfm) = %{tl_version}
Provides:       tex(mdwciric8t.tfm) = %{tl_version}, tex(mdxcib7t.tfm) = %{tl_version}
Provides:       tex(mdxcib7y.tfm) = %{tl_version}, tex(mdxcib8t.tfm) = %{tl_version}
Provides:       tex(mdxcibc8t.tfm) = %{tl_version}, tex(mdxcibi7t.tfm) = %{tl_version}
Provides:       tex(mdxcibi7y.tfm) = %{tl_version}, tex(mdxcibi8t.tfm) = %{tl_version}
Provides:       tex(mdxcibic8t.tfm) = %{tl_version}, tex(mdxcic7t.tfm) = %{tl_version}
Provides:       tex(mdxcic7y.tfm) = %{tl_version}, tex(mdxcic8t.tfm) = %{tl_version}
Provides:       tex(mdxcicc8t.tfm) = %{tl_version}, tex(mdxcici7t.tfm) = %{tl_version}
Provides:       tex(mdxcici7y.tfm) = %{tl_version}, tex(mdxcici8t.tfm) = %{tl_version}
Provides:       tex(mdxcicic8t.tfm) = %{tl_version}, tex(mdxcir7t.tfm) = %{tl_version}
Provides:       tex(mdxcir7y.tfm) = %{tl_version}, tex(mdxcir8t.tfm) = %{tl_version}
Provides:       tex(mdxcirc8t.tfm) = %{tl_version}, tex(mdxciri7t.tfm) = %{tl_version}
Provides:       tex(mdxciri7y.tfm) = %{tl_version}, tex(mdxciri8t.tfm) = %{tl_version}
Provides:       tex(mdxciric8t.tfm) = %{tl_version}, tex(md-gdr7m.tfm) = %{tl_version}
Provides:       tex(md-gdr7t.tfm) = %{tl_version}, tex(md-gdr7v.tfm) = %{tl_version}
Provides:       tex(md-gdr7y.tfm) = %{tl_version}, tex(md-gdr8c.tfm) = %{tl_version}
Provides:       tex(md-gdr8t.tfm) = %{tl_version}, tex(md-gdree.tfm) = %{tl_version}
Provides:       tex(md-gdri7m.tfm) = %{tl_version}, tex(md-gdri7t.tfm) = %{tl_version}
Provides:       tex(md-gdri8c.tfm) = %{tl_version}, tex(md-gdri8t.tfm) = %{tl_version}
Provides:       tex(md-gdrma.tfm) = %{tl_version}, tex(md-gdrmb.tfm) = %{tl_version}
Provides:       tex(md-gds7m.tfm) = %{tl_version}, tex(md-gds7t.tfm) = %{tl_version}
Provides:       tex(md-gds7v.tfm) = %{tl_version}, tex(md-gds7y.tfm) = %{tl_version}
Provides:       tex(md-gds8c.tfm) = %{tl_version}, tex(md-gds8t.tfm) = %{tl_version}
Provides:       tex(md-gdsi7m.tfm) = %{tl_version}, tex(md-gdsi7t.tfm) = %{tl_version}
Provides:       tex(md-gdsi8c.tfm) = %{tl_version}, tex(md-gdsi8t.tfm) = %{tl_version}
Provides:       tex(md-gdsma.tfm) = %{tl_version}, tex(md-gdsmb.tfm) = %{tl_version}
Provides:       tex(mdpgdb8c.tfm) = %{tl_version}, tex(mdpgdb8t.tfm) = %{tl_version}
Provides:       tex(mdpgdbc8c.tfm) = %{tl_version}, tex(mdpgdbc8t.tfm) = %{tl_version}
Provides:       tex(mdpgdbfc8t.tfm) = %{tl_version}, tex(mdpgdbi8c.tfm) = %{tl_version}
Provides:       tex(mdpgdbi8t.tfm) = %{tl_version}, tex(mdpgdbic8c.tfm) = %{tl_version}
Provides:       tex(mdpgdbic8t.tfm) = %{tl_version}, tex(mdpgdbifc8t.tfm) = %{tl_version}
Provides:       tex(mdpgdr7m.tfm) = %{tl_version}, tex(mdpgdr7t.tfm) = %{tl_version}
Provides:       tex(mdpgdr7v.tfm) = %{tl_version}, tex(mdpgdr7y.tfm) = %{tl_version}
Provides:       tex(mdpgdr8c.tfm) = %{tl_version}, tex(mdpgdr8t.tfm) = %{tl_version}
Provides:       tex(mdpgdrc8c.tfm) = %{tl_version}, tex(mdpgdrc8t.tfm) = %{tl_version}
Provides:       tex(mdpgdrfc8t.tfm) = %{tl_version}, tex(mdpgdri7m.tfm) = %{tl_version}
Provides:       tex(mdpgdri7t.tfm) = %{tl_version}, tex(mdpgdri8c.tfm) = %{tl_version}
Provides:       tex(mdpgdri8t.tfm) = %{tl_version}, tex(mdpgdric8c.tfm) = %{tl_version}
Provides:       tex(mdpgdric8t.tfm) = %{tl_version}, tex(mdpgdrifc8t.tfm) = %{tl_version}
Provides:       tex(mdpgdrma.tfm) = %{tl_version}, tex(mdpgdrmb.tfm) = %{tl_version}
Provides:       tex(mdpgds7m.tfm) = %{tl_version}, tex(mdpgds7t.tfm) = %{tl_version}
Provides:       tex(mdpgds7v.tfm) = %{tl_version}, tex(mdpgds7y.tfm) = %{tl_version}
Provides:       tex(mdpgds8c.tfm) = %{tl_version}, tex(mdpgds8t.tfm) = %{tl_version}
Provides:       tex(mdpgdsc8c.tfm) = %{tl_version}, tex(mdpgdsc8t.tfm) = %{tl_version}
Provides:       tex(mdpgdsfc8t.tfm) = %{tl_version}, tex(mdpgdsi7m.tfm) = %{tl_version}
Provides:       tex(mdpgdsi7t.tfm) = %{tl_version}, tex(mdpgdsi8c.tfm) = %{tl_version}
Provides:       tex(mdpgdsi8t.tfm) = %{tl_version}, tex(mdpgdsic8c.tfm) = %{tl_version}
Provides:       tex(mdpgdsic8t.tfm) = %{tl_version}, tex(mdpgdsifc8t.tfm) = %{tl_version}
Provides:       tex(mdpgdsma.tfm) = %{tl_version}, tex(mdpgdsmb.tfm) = %{tl_version}
Provides:       tex(mdwgdb7m.tfm) = %{tl_version}, tex(mdwgdb7y.tfm) = %{tl_version}
Provides:       tex(mdwgdb8t.tfm) = %{tl_version}, tex(mdwgdbc8t.tfm) = %{tl_version}
Provides:       tex(mdwgdbi7m.tfm) = %{tl_version}, tex(mdwgdbi7y.tfm) = %{tl_version}
Provides:       tex(mdwgdbi8t.tfm) = %{tl_version}, tex(mdwgdbic8t.tfm) = %{tl_version}
Provides:       tex(mdwgdr7m.tfm) = %{tl_version}, tex(mdwgdr7y.tfm) = %{tl_version}
Provides:       tex(mdwgdr8t.tfm) = %{tl_version}, tex(mdwgdrc8t.tfm) = %{tl_version}
Provides:       tex(mdwgdri7m.tfm) = %{tl_version}, tex(mdwgdri7y.tfm) = %{tl_version}
Provides:       tex(mdwgdri8t.tfm) = %{tl_version}, tex(mdwgdric8t.tfm) = %{tl_version}
Provides:       tex(mdwgds7m.tfm) = %{tl_version}, tex(mdwgds7y.tfm) = %{tl_version}
Provides:       tex(mdwgds8t.tfm) = %{tl_version}, tex(mdwgdsc8t.tfm) = %{tl_version}
Provides:       tex(mdwgdsi7m.tfm) = %{tl_version}, tex(mdwgdsi7y.tfm) = %{tl_version}
Provides:       tex(mdwgdsi8t.tfm) = %{tl_version}, tex(mdwgdsic8t.tfm) = %{tl_version}
Provides:       tex(mdxgdb7t.tfm) = %{tl_version}, tex(mdxgdb7y.tfm) = %{tl_version}
Provides:       tex(mdxgdb8t.tfm) = %{tl_version}, tex(mdxgdbc8t.tfm) = %{tl_version}
Provides:       tex(mdxgdbi7t.tfm) = %{tl_version}, tex(mdxgdbi7y.tfm) = %{tl_version}
Provides:       tex(mdxgdbi8t.tfm) = %{tl_version}, tex(mdxgdbic8t.tfm) = %{tl_version}
Provides:       tex(mdxgdr7t.tfm) = %{tl_version}, tex(mdxgdr7y.tfm) = %{tl_version}
Provides:       tex(mdxgdr8t.tfm) = %{tl_version}, tex(mdxgdrc8t.tfm) = %{tl_version}
Provides:       tex(mdxgdri7t.tfm) = %{tl_version}, tex(mdxgdri7y.tfm) = %{tl_version}
Provides:       tex(mdxgdri8t.tfm) = %{tl_version}, tex(mdxgdric8t.tfm) = %{tl_version}
Provides:       tex(mdxgds7t.tfm) = %{tl_version}, tex(mdxgds7y.tfm) = %{tl_version}
Provides:       tex(mdxgds8t.tfm) = %{tl_version}, tex(mdxgdsc8t.tfm) = %{tl_version}
Provides:       tex(mdxgdsi7t.tfm) = %{tl_version}, tex(mdxgdsi7y.tfm) = %{tl_version}
Provides:       tex(mdxgdsi8t.tfm) = %{tl_version}, tex(mdxgdsic8t.tfm) = %{tl_version}
Provides:       tex(md-usr7m.tfm) = %{tl_version}, tex(md-usr7t.tfm) = %{tl_version}
Provides:       tex(md-usr7t5.tfm) = %{tl_version}, tex(md-usr7t6.tfm) = %{tl_version}
Provides:       tex(md-usr7t7.tfm) = %{tl_version}, tex(md-usr7t8.tfm) = %{tl_version}
Provides:       tex(md-usr7t9.tfm) = %{tl_version}, tex(md-usr7v.tfm) = %{tl_version}
Provides:       tex(md-usr7y.tfm) = %{tl_version}, tex(md-usr8c.tfm) = %{tl_version}
Provides:       tex(md-usr8t.tfm) = %{tl_version}, tex(md-usree.tfm) = %{tl_version}
Provides:       tex(md-usri7m.tfm) = %{tl_version}, tex(md-usri7t.tfm) = %{tl_version}
Provides:       tex(md-usri7t5.tfm) = %{tl_version}, tex(md-usri7t6.tfm) = %{tl_version}
Provides:       tex(md-usri7t7.tfm) = %{tl_version}, tex(md-usri7t8.tfm) = %{tl_version}
Provides:       tex(md-usri7t9.tfm) = %{tl_version}, tex(md-usri8c.tfm) = %{tl_version}
Provides:       tex(md-usri8t.tfm) = %{tl_version}, tex(md-usrma.tfm) = %{tl_version}
Provides:       tex(md-usrmb.tfm) = %{tl_version}, tex(md-uss7m.tfm) = %{tl_version}
Provides:       tex(md-uss7t.tfm) = %{tl_version}, tex(md-uss7v.tfm) = %{tl_version}
Provides:       tex(md-uss7y.tfm) = %{tl_version}, tex(md-uss8c.tfm) = %{tl_version}
Provides:       tex(md-uss8t.tfm) = %{tl_version}, tex(md-ussi7m.tfm) = %{tl_version}
Provides:       tex(md-ussi7t.tfm) = %{tl_version}, tex(md-ussi8c.tfm) = %{tl_version}
Provides:       tex(md-ussi8t.tfm) = %{tl_version}, tex(md-ussma.tfm) = %{tl_version}
Provides:       tex(md-ussmb.tfm) = %{tl_version}, tex(mdpusb8c.tfm) = %{tl_version}
Provides:       tex(mdpusb8t.tfm) = %{tl_version}, tex(mdpusbc8c.tfm) = %{tl_version}
Provides:       tex(mdpusbc8t.tfm) = %{tl_version}, tex(mdpusbfc8t.tfm) = %{tl_version}
Provides:       tex(mdpusbi8c.tfm) = %{tl_version}, tex(mdpusbi8t.tfm) = %{tl_version}
Provides:       tex(mdpusbic8c.tfm) = %{tl_version}, tex(mdpusbic8t.tfm) = %{tl_version}
Provides:       tex(mdpusbifc8t.tfm) = %{tl_version}, tex(mdpusr7m.tfm) = %{tl_version}
Provides:       tex(mdpusr7t.tfm) = %{tl_version}, tex(mdpusr7v.tfm) = %{tl_version}
Provides:       tex(mdpusr7y.tfm) = %{tl_version}, tex(mdpusr8c.tfm) = %{tl_version}
Provides:       tex(mdpusr8t.tfm) = %{tl_version}, tex(mdpusrc8c.tfm) = %{tl_version}
Provides:       tex(mdpusrc8t.tfm) = %{tl_version}, tex(mdpusrfc8t.tfm) = %{tl_version}
Provides:       tex(mdpusri7m.tfm) = %{tl_version}, tex(mdpusri7t.tfm) = %{tl_version}
Provides:       tex(mdpusri8c.tfm) = %{tl_version}, tex(mdpusri8t.tfm) = %{tl_version}
Provides:       tex(mdpusric8c.tfm) = %{tl_version}, tex(mdpusric8t.tfm) = %{tl_version}
Provides:       tex(mdpusrifc8t.tfm) = %{tl_version}, tex(mdpusrma.tfm) = %{tl_version}
Provides:       tex(mdpusrmb.tfm) = %{tl_version}, tex(mdpuss7m.tfm) = %{tl_version}
Provides:       tex(mdpuss7t.tfm) = %{tl_version}, tex(mdpuss7v.tfm) = %{tl_version}
Provides:       tex(mdpuss7y.tfm) = %{tl_version}, tex(mdpuss8c.tfm) = %{tl_version}
Provides:       tex(mdpuss8t.tfm) = %{tl_version}, tex(mdpussc8c.tfm) = %{tl_version}
Provides:       tex(mdpussc8t.tfm) = %{tl_version}, tex(mdpussfc8t.tfm) = %{tl_version}
Provides:       tex(mdpussi7m.tfm) = %{tl_version}, tex(mdpussi7t.tfm) = %{tl_version}
Provides:       tex(mdpussi8c.tfm) = %{tl_version}, tex(mdpussi8t.tfm) = %{tl_version}
Provides:       tex(mdpussic8c.tfm) = %{tl_version}, tex(mdpussic8t.tfm) = %{tl_version}
Provides:       tex(mdpussifc8t.tfm) = %{tl_version}, tex(mdpussma.tfm) = %{tl_version}
Provides:       tex(mdpussmb.tfm) = %{tl_version}, tex(mdwusb7m.tfm) = %{tl_version}
Provides:       tex(mdwusb7y.tfm) = %{tl_version}, tex(mdwusb8t.tfm) = %{tl_version}
Provides:       tex(mdwusbc8t.tfm) = %{tl_version}, tex(mdwusbi7m.tfm) = %{tl_version}
Provides:       tex(mdwusbi7y.tfm) = %{tl_version}, tex(mdwusbi8t.tfm) = %{tl_version}
Provides:       tex(mdwusbic8t.tfm) = %{tl_version}, tex(mdwusr7m.tfm) = %{tl_version}
Provides:       tex(mdwusr7y.tfm) = %{tl_version}, tex(mdwusr8t.tfm) = %{tl_version}
Provides:       tex(mdwusrc8t.tfm) = %{tl_version}, tex(mdwusri7m.tfm) = %{tl_version}
Provides:       tex(mdwusri7y.tfm) = %{tl_version}, tex(mdwusri8t.tfm) = %{tl_version}
Provides:       tex(mdwusric8t.tfm) = %{tl_version}, tex(mdwuss7m.tfm) = %{tl_version}
Provides:       tex(mdwuss7y.tfm) = %{tl_version}, tex(mdwuss8t.tfm) = %{tl_version}
Provides:       tex(mdwussc8t.tfm) = %{tl_version}, tex(mdwussi7m.tfm) = %{tl_version}
Provides:       tex(mdwussi7y.tfm) = %{tl_version}, tex(mdwussi8t.tfm) = %{tl_version}
Provides:       tex(mdwussic8t.tfm) = %{tl_version}, tex(mdxusb7t.tfm) = %{tl_version}
Provides:       tex(mdxusb7y.tfm) = %{tl_version}, tex(mdxusb8t.tfm) = %{tl_version}
Provides:       tex(mdxusbc8t.tfm) = %{tl_version}, tex(mdxusbi7t.tfm) = %{tl_version}
Provides:       tex(mdxusbi7y.tfm) = %{tl_version}, tex(mdxusbi8t.tfm) = %{tl_version}
Provides:       tex(mdxusbic8t.tfm) = %{tl_version}, tex(mdxusr7t.tfm) = %{tl_version}
Provides:       tex(mdxusr7y.tfm) = %{tl_version}, tex(mdxusr8t.tfm) = %{tl_version}
Provides:       tex(mdxusrc8t.tfm) = %{tl_version}, tex(mdxusri7t.tfm) = %{tl_version}
Provides:       tex(mdxusri7y.tfm) = %{tl_version}, tex(mdxusri8t.tfm) = %{tl_version}
Provides:       tex(mdxusric8t.tfm) = %{tl_version}, tex(mdxuss7t.tfm) = %{tl_version}
Provides:       tex(mdxuss7y.tfm) = %{tl_version}, tex(mdxuss8t.tfm) = %{tl_version}
Provides:       tex(mdxussc8t.tfm) = %{tl_version}, tex(mdxussi7t.tfm) = %{tl_version}
Provides:       tex(mdxussi7y.tfm) = %{tl_version}, tex(mdxussi8t.tfm) = %{tl_version}
Provides:       tex(mdxussic8t.tfm) = %{tl_version}, tex(md-utb7m.tfm) = %{tl_version}
Provides:       tex(md-utb7t.tfm) = %{tl_version}, tex(md-utb7v.tfm) = %{tl_version}
Provides:       tex(md-utb7y.tfm) = %{tl_version}, tex(md-utb8c.tfm) = %{tl_version}
Provides:       tex(md-utb8t.tfm) = %{tl_version}, tex(md-utb8y.tfm) = %{tl_version}
Provides:       tex(md-utbee.tfm) = %{tl_version}, tex(md-utbi7m.tfm) = %{tl_version}
Provides:       tex(md-utbi7t.tfm) = %{tl_version}, tex(md-utbi8c.tfm) = %{tl_version}
Provides:       tex(md-utbi8t.tfm) = %{tl_version}, tex(md-utbi8y.tfm) = %{tl_version}
Provides:       tex(md-utbma.tfm) = %{tl_version}, tex(md-utbmb.tfm) = %{tl_version}
Provides:       tex(md-utbo7t.tfm) = %{tl_version}, tex(md-utbo8c.tfm) = %{tl_version}
Provides:       tex(md-utbo8t.tfm) = %{tl_version}, tex(md-utbo8y.tfm) = %{tl_version}
Provides:       tex(md-utr7m.tfm) = %{tl_version}, tex(md-utr7t.tfm) = %{tl_version}
Provides:       tex(md-utr7v.tfm) = %{tl_version}, tex(md-utr7y.tfm) = %{tl_version}
Provides:       tex(md-utr8c.tfm) = %{tl_version}, tex(md-utr8t.tfm) = %{tl_version}
Provides:       tex(md-utr8y.tfm) = %{tl_version}, tex(md-utree.tfm) = %{tl_version}
Provides:       tex(md-utri7m.tfm) = %{tl_version}, tex(md-utri7t.tfm) = %{tl_version}
Provides:       tex(md-utri8c.tfm) = %{tl_version}, tex(md-utri8t.tfm) = %{tl_version}
Provides:       tex(md-utri8y.tfm) = %{tl_version}, tex(md-utrma.tfm) = %{tl_version}
Provides:       tex(md-utrmb.tfm) = %{tl_version}, tex(md-utro7t.tfm) = %{tl_version}
Provides:       tex(md-utro8c.tfm) = %{tl_version}, tex(md-utro8t.tfm) = %{tl_version}
Provides:       tex(md-utro8y.tfm) = %{tl_version}, tex(mdputb7m.tfm) = %{tl_version}
Provides:       tex(mdputb7t.tfm) = %{tl_version}, tex(mdputb7v.tfm) = %{tl_version}
Provides:       tex(mdputb7y.tfm) = %{tl_version}, tex(mdputb8c.tfm) = %{tl_version}
Provides:       tex(mdputb8t.tfm) = %{tl_version}, tex(mdputbc8t.tfm) = %{tl_version}
Provides:       tex(mdputbfc8t.tfm) = %{tl_version}, tex(mdputbi7m.tfm) = %{tl_version}
Provides:       tex(mdputbi7t.tfm) = %{tl_version}, tex(mdputbi8c.tfm) = %{tl_version}
Provides:       tex(mdputbi8t.tfm) = %{tl_version}, tex(mdputbifc8t.tfm) = %{tl_version}
Provides:       tex(mdputbma.tfm) = %{tl_version}, tex(mdputbmb.tfm) = %{tl_version}
Provides:       tex(mdputbo7t.tfm) = %{tl_version}, tex(mdputbo8c.tfm) = %{tl_version}
Provides:       tex(mdputbo8t.tfm) = %{tl_version}, tex(mdputbofc8t.tfm) = %{tl_version}
Provides:       tex(mdputr7m.tfm) = %{tl_version}, tex(mdputr7t.tfm) = %{tl_version}
Provides:       tex(mdputr7v.tfm) = %{tl_version}, tex(mdputr7y.tfm) = %{tl_version}
Provides:       tex(mdputr8c.tfm) = %{tl_version}, tex(mdputr8t.tfm) = %{tl_version}
Provides:       tex(mdputrc8t.tfm) = %{tl_version}, tex(mdputrfc8t.tfm) = %{tl_version}
Provides:       tex(mdputri7m.tfm) = %{tl_version}, tex(mdputri7t.tfm) = %{tl_version}
Provides:       tex(mdputri8c.tfm) = %{tl_version}, tex(mdputri8t.tfm) = %{tl_version}
Provides:       tex(mdputrifc8t.tfm) = %{tl_version}, tex(mdputrma.tfm) = %{tl_version}
Provides:       tex(mdputrmb.tfm) = %{tl_version}, tex(mdputro7t.tfm) = %{tl_version}
Provides:       tex(mdputro8c.tfm) = %{tl_version}, tex(mdputro8t.tfm) = %{tl_version}
Provides:       tex(mdputrofc8t.tfm) = %{tl_version}, tex(putb8a.tfm) = %{tl_version}
Provides:       tex(putb8x.tfm) = %{tl_version}, tex(putbi8a.tfm) = %{tl_version}
Provides:       tex(putr8a.tfm) = %{tl_version}, tex(putr8x.tfm) = %{tl_version}
Provides:       tex(putri8a.tfm) = %{tl_version}, tex(md-gmm7m.tfm) = %{tl_version}
Provides:       tex(md-gmm7t.tfm) = %{tl_version}, tex(md-gmm7v.tfm) = %{tl_version}
Provides:       tex(md-gmm7y.tfm) = %{tl_version}, tex(md-gmm8c.tfm) = %{tl_version}
Provides:       tex(md-gmm8t.tfm) = %{tl_version}, tex(md-gmm8y.tfm) = %{tl_version}
Provides:       tex(md-gmmi7m.tfm) = %{tl_version}, tex(md-gmmi7t.tfm) = %{tl_version}
Provides:       tex(md-gmmi8c.tfm) = %{tl_version}, tex(md-gmmi8t.tfm) = %{tl_version}
Provides:       tex(md-gmmi8y.tfm) = %{tl_version}, tex(md-gmmma.tfm) = %{tl_version}
Provides:       tex(md-gmmmb.tfm) = %{tl_version}, tex(md-gmmo7t.tfm) = %{tl_version}
Provides:       tex(md-gmmo8c.tfm) = %{tl_version}, tex(md-gmmo8t.tfm) = %{tl_version}
Provides:       tex(md-gmmo8y.tfm) = %{tl_version}, tex(md-gmr7m.tfm) = %{tl_version}
Provides:       tex(md-gmr7t.tfm) = %{tl_version}, tex(md-gmr7v.tfm) = %{tl_version}
Provides:       tex(md-gmr7y.tfm) = %{tl_version}, tex(md-gmr8c.tfm) = %{tl_version}
Provides:       tex(md-gmr8t.tfm) = %{tl_version}, tex(md-gmr8y.tfm) = %{tl_version}
Provides:       tex(md-gmree.tfm) = %{tl_version}, tex(md-gmri7m.tfm) = %{tl_version}
Provides:       tex(md-gmri7t.tfm) = %{tl_version}, tex(md-gmri8c.tfm) = %{tl_version}
Provides:       tex(md-gmri8t.tfm) = %{tl_version}, tex(md-gmri8y.tfm) = %{tl_version}
Provides:       tex(md-gmrma.tfm) = %{tl_version}, tex(md-gmrmb.tfm) = %{tl_version}
Provides:       tex(md-gmro7t.tfm) = %{tl_version}, tex(md-gmro8c.tfm) = %{tl_version}
Provides:       tex(md-gmro8t.tfm) = %{tl_version}, tex(md-gmro8y.tfm) = %{tl_version}
Provides:       tex(mdugmm7m.tfm) = %{tl_version}, tex(mdugmm7t.tfm) = %{tl_version}
Provides:       tex(mdugmm7v.tfm) = %{tl_version}, tex(mdugmm7y.tfm) = %{tl_version}
Provides:       tex(mdugmm8c.tfm) = %{tl_version}, tex(mdugmm8t.tfm) = %{tl_version}
Provides:       tex(mdugmmfc8t.tfm) = %{tl_version}, tex(mdugmmi7m.tfm) = %{tl_version}
Provides:       tex(mdugmmi7t.tfm) = %{tl_version}, tex(mdugmmi8c.tfm) = %{tl_version}
Provides:       tex(mdugmmi8t.tfm) = %{tl_version}, tex(mdugmmifc8t.tfm) = %{tl_version}
Provides:       tex(mdugmmma.tfm) = %{tl_version}, tex(mdugmmmb.tfm) = %{tl_version}
Provides:       tex(mdugmmo7t.tfm) = %{tl_version}, tex(mdugmmo8c.tfm) = %{tl_version}
Provides:       tex(mdugmmo8t.tfm) = %{tl_version}, tex(mdugmmofc8t.tfm) = %{tl_version}
Provides:       tex(mdugmr7m.tfm) = %{tl_version}, tex(mdugmr7t.tfm) = %{tl_version}
Provides:       tex(mdugmr7v.tfm) = %{tl_version}, tex(mdugmr7y.tfm) = %{tl_version}
Provides:       tex(mdugmr8c.tfm) = %{tl_version}, tex(mdugmr8t.tfm) = %{tl_version}
Provides:       tex(mdugmrfc8t.tfm) = %{tl_version}, tex(mdugmri7m.tfm) = %{tl_version}
Provides:       tex(mdugmri7t.tfm) = %{tl_version}, tex(mdugmri8c.tfm) = %{tl_version}
Provides:       tex(mdugmri8t.tfm) = %{tl_version}, tex(mdugmrifc8t.tfm) = %{tl_version}
Provides:       tex(mdugmrma.tfm) = %{tl_version}, tex(mdugmrmb.tfm) = %{tl_version}
Provides:       tex(mdugmro7t.tfm) = %{tl_version}, tex(mdugmro8c.tfm) = %{tl_version}
Provides:       tex(mdugmro8t.tfm) = %{tl_version}, tex(mdugmrofc8t.tfm) = %{tl_version}
Provides:       tex(ugmm8a.tfm) = %{tl_version}, tex(ugmmi8a.tfm) = %{tl_version}
Provides:       tex(ugmr8a.tfm) = %{tl_version}, tex(ugmri8a.tfm) = %{tl_version}
Provides:       tex(md-chb7m.pfb) = %{tl_version}, tex(md-chb7t.pfb) = %{tl_version}
Provides:       tex(md-chb7v.pfb) = %{tl_version}, tex(md-chb7y.pfb) = %{tl_version}
Provides:       tex(md-chb8c.pfb) = %{tl_version}, tex(md-chb8t.pfb) = %{tl_version}
Provides:       tex(md-chbi7m.pfb) = %{tl_version}, tex(md-chbi7t.pfb) = %{tl_version}
Provides:       tex(md-chbi8c.pfb) = %{tl_version}, tex(md-chbi8t.pfb) = %{tl_version}
Provides:       tex(md-chbma.pfb) = %{tl_version}, tex(md-chbmb.pfb) = %{tl_version}
Provides:       tex(md-chr7m.pfb) = %{tl_version}, tex(md-chr7t.pfb) = %{tl_version}
Provides:       tex(md-chr7v.pfb) = %{tl_version}, tex(md-chr7y.pfb) = %{tl_version}
Provides:       tex(md-chr8c.pfb) = %{tl_version}, tex(md-chr8t.pfb) = %{tl_version}
Provides:       tex(md-chree.pfb) = %{tl_version}, tex(md-chri7m.pfb) = %{tl_version}
Provides:       tex(md-chri7t.pfb) = %{tl_version}, tex(md-chri8c.pfb) = %{tl_version}
Provides:       tex(md-chri8t.pfb) = %{tl_version}, tex(md-chrma.pfb) = %{tl_version}
Provides:       tex(md-chrmb.pfb) = %{tl_version}, tex(UtopiaStd-Regular.pfb) = %{tl_version}
Provides:       tex(md-cib7m.pfb) = %{tl_version}, tex(md-cib7t.pfb) = %{tl_version}
Provides:       tex(md-cib7v.pfb) = %{tl_version}, tex(md-cib7y.pfb) = %{tl_version}
Provides:       tex(md-cib8c.pfb) = %{tl_version}, tex(md-cib8t.pfb) = %{tl_version}
Provides:       tex(md-cibee.pfb) = %{tl_version}, tex(md-cibi7m.pfb) = %{tl_version}
Provides:       tex(md-cibi7t.pfb) = %{tl_version}, tex(md-cibi8c.pfb) = %{tl_version}
Provides:       tex(md-cibi8t.pfb) = %{tl_version}, tex(md-cibma.pfb) = %{tl_version}
Provides:       tex(md-cibmb.pfb) = %{tl_version}, tex(md-cir7m.pfb) = %{tl_version}
Provides:       tex(md-cir7t.pfb) = %{tl_version}, tex(md-cir7v.pfb) = %{tl_version}
Provides:       tex(md-cir7y.pfb) = %{tl_version}, tex(md-cir8c.pfb) = %{tl_version}
Provides:       tex(md-cir8t.pfb) = %{tl_version}, tex(md-ciree.pfb) = %{tl_version}
Provides:       tex(md-ciri7m.pfb) = %{tl_version}, tex(md-ciri7t.pfb) = %{tl_version}
Provides:       tex(md-ciri8c.pfb) = %{tl_version}, tex(md-ciri8t.pfb) = %{tl_version}
Provides:       tex(md-cirma.pfb) = %{tl_version}, tex(md-cirmb.pfb) = %{tl_version}
Provides:       tex(md-gdr7m.pfb) = %{tl_version}, tex(md-gdr7t.pfb) = %{tl_version}
Provides:       tex(md-gdr7v.pfb) = %{tl_version}, tex(md-gdr7y.pfb) = %{tl_version}
Provides:       tex(md-gdr8c.pfb) = %{tl_version}, tex(md-gdr8t.pfb) = %{tl_version}
Provides:       tex(md-gdree.pfb) = %{tl_version}, tex(md-gdri7m.pfb) = %{tl_version}
Provides:       tex(md-gdri7t.pfb) = %{tl_version}, tex(md-gdri8c.pfb) = %{tl_version}
Provides:       tex(md-gdri8t.pfb) = %{tl_version}, tex(md-gdrma.pfb) = %{tl_version}
Provides:       tex(md-gdrmb.pfb) = %{tl_version}, tex(md-gds7m.pfb) = %{tl_version}
Provides:       tex(md-gds7t.pfb) = %{tl_version}, tex(md-gds7v.pfb) = %{tl_version}
Provides:       tex(md-gds7y.pfb) = %{tl_version}, tex(md-gds8c.pfb) = %{tl_version}
Provides:       tex(md-gds8t.pfb) = %{tl_version}, tex(md-gdsi7m.pfb) = %{tl_version}
Provides:       tex(md-gdsi7t.pfb) = %{tl_version}, tex(md-gdsi8c.pfb) = %{tl_version}
Provides:       tex(md-gdsi8t.pfb) = %{tl_version}, tex(md-gdsma.pfb) = %{tl_version}
Provides:       tex(md-gdsmb.pfb) = %{tl_version}, tex(md-utrma.pfb) = %{tl_version}
Provides:       tex(md-usr7m.pfb) = %{tl_version}, tex(md-usr7t.pfb) = %{tl_version}
Provides:       tex(md-usr7t5.pfb) = %{tl_version}, tex(md-usr7t6.pfb) = %{tl_version}
Provides:       tex(md-usr7t7.pfb) = %{tl_version}, tex(md-usr7t8.pfb) = %{tl_version}
Provides:       tex(md-usr7t9.pfb) = %{tl_version}, tex(md-usr7v.pfb) = %{tl_version}
Provides:       tex(md-usr7y.pfb) = %{tl_version}, tex(md-usr8c.pfb) = %{tl_version}
Provides:       tex(md-usr8t.pfb) = %{tl_version}, tex(md-usree.pfb) = %{tl_version}
Provides:       tex(md-usri7m.pfb) = %{tl_version}, tex(md-usri7t.pfb) = %{tl_version}
Provides:       tex(md-usri7t5.pfb) = %{tl_version}, tex(md-usri7t6.pfb) = %{tl_version}
Provides:       tex(md-usri7t7.pfb) = %{tl_version}, tex(md-usri7t8.pfb) = %{tl_version}
Provides:       tex(md-usri7t9.pfb) = %{tl_version}, tex(md-usri8c.pfb) = %{tl_version}
Provides:       tex(md-usri8t.pfb) = %{tl_version}, tex(md-usrma.pfb) = %{tl_version}
Provides:       tex(md-usrmb.pfb) = %{tl_version}, tex(md-uss7m.pfb) = %{tl_version}
Provides:       tex(md-uss7t.pfb) = %{tl_version}, tex(md-uss7v.pfb) = %{tl_version}
Provides:       tex(md-uss7y.pfb) = %{tl_version}, tex(md-uss8c.pfb) = %{tl_version}
Provides:       tex(md-uss8t.pfb) = %{tl_version}, tex(md-ussi7m.pfb) = %{tl_version}
Provides:       tex(md-ussi7t.pfb) = %{tl_version}, tex(md-ussi8c.pfb) = %{tl_version}
Provides:       tex(md-ussi8t.pfb) = %{tl_version}, tex(md-ussma.pfb) = %{tl_version}
Provides:       tex(md-ussmb.pfb) = %{tl_version}, tex(md-utb7m.pfb) = %{tl_version}
Provides:       tex(md-utb7t.pfb) = %{tl_version}, tex(md-utb7v.pfb) = %{tl_version}
Provides:       tex(md-utb7y.pfb) = %{tl_version}, tex(md-utb8c.pfb) = %{tl_version}
Provides:       tex(md-utb8t.pfb) = %{tl_version}, tex(md-utbee.pfb) = %{tl_version}
Provides:       tex(md-utbi7m.pfb) = %{tl_version}, tex(md-utbi7t.pfb) = %{tl_version}
Provides:       tex(md-utbi8c.pfb) = %{tl_version}, tex(md-utbi8t.pfb) = %{tl_version}
Provides:       tex(md-utbma.pfb) = %{tl_version}, tex(md-utbmb.pfb) = %{tl_version}
Provides:       tex(md-utr7m.pfb) = %{tl_version}, tex(md-utr7t.pfb) = %{tl_version}
Provides:       tex(md-utr7v.pfb) = %{tl_version}, tex(md-utr7y.pfb) = %{tl_version}
Provides:       tex(md-utr8c.pfb) = %{tl_version}, tex(md-utr8t.pfb) = %{tl_version}
Provides:       tex(md-utree.pfb) = %{tl_version}, tex(md-utri7m.pfb) = %{tl_version}
Provides:       tex(md-utri7t.pfb) = %{tl_version}, tex(md-utri8c.pfb) = %{tl_version}
Provides:       tex(md-utri8t.pfb) = %{tl_version}, tex(md-utrma.pfb) = %{tl_version}
Provides:       tex(md-utrmb.pfb) = %{tl_version}, tex(md-gmm7m.pfb) = %{tl_version}
Provides:       tex(md-gmm7t.pfb) = %{tl_version}, tex(md-gmm7v.pfb) = %{tl_version}
Provides:       tex(md-gmm7y.pfb) = %{tl_version}, tex(md-gmm8c.pfb) = %{tl_version}
Provides:       tex(md-gmm8t.pfb) = %{tl_version}, tex(md-gmmi7m.pfb) = %{tl_version}
Provides:       tex(md-gmmi7t.pfb) = %{tl_version}, tex(md-gmmi8c.pfb) = %{tl_version}
Provides:       tex(md-gmmi8t.pfb) = %{tl_version}, tex(md-gmmma.pfb) = %{tl_version}
Provides:       tex(md-gmmmb.pfb) = %{tl_version}, tex(md-gmr7m.pfb) = %{tl_version}
Provides:       tex(md-gmr7t.pfb) = %{tl_version}, tex(md-gmr7v.pfb) = %{tl_version}
Provides:       tex(md-gmr7y.pfb) = %{tl_version}, tex(md-gmr8c.pfb) = %{tl_version}
Provides:       tex(md-gmr8t.pfb) = %{tl_version}, tex(md-gmree.pfb) = %{tl_version}
Provides:       tex(md-gmri7m.pfb) = %{tl_version}, tex(md-gmri7t.pfb) = %{tl_version}
Provides:       tex(md-gmri8c.pfb) = %{tl_version}, tex(md-gmri8t.pfb) = %{tl_version}
Provides:       tex(md-gmrma.pfb) = %{tl_version}, tex(md-gmrmb.pfb) = %{tl_version}
Provides:       tex(mdbchb7m.vf) = %{tl_version}, tex(mdbchb7t.vf) = %{tl_version}
Provides:       tex(mdbchb7v.vf) = %{tl_version}, tex(mdbchb7y.vf) = %{tl_version}
Provides:       tex(mdbchb8c.vf) = %{tl_version}, tex(mdbchb8t.vf) = %{tl_version}
Provides:       tex(mdbchbc8t.vf) = %{tl_version}, tex(mdbchbfc8t.vf) = %{tl_version}
Provides:       tex(mdbchbi7m.vf) = %{tl_version}, tex(mdbchbi7t.vf) = %{tl_version}
Provides:       tex(mdbchbi8c.vf) = %{tl_version}, tex(mdbchbi8t.vf) = %{tl_version}
Provides:       tex(mdbchbifc8t.vf) = %{tl_version}, tex(mdbchbma.vf) = %{tl_version}
Provides:       tex(mdbchbmb.vf) = %{tl_version}, tex(mdbchbo7t.vf) = %{tl_version}
Provides:       tex(mdbchbo8c.vf) = %{tl_version}, tex(mdbchbo8t.vf) = %{tl_version}
Provides:       tex(mdbchbofc8t.vf) = %{tl_version}, tex(mdbchr7m.vf) = %{tl_version}
Provides:       tex(mdbchr7t.vf) = %{tl_version}, tex(mdbchr7v.vf) = %{tl_version}
Provides:       tex(mdbchr7y.vf) = %{tl_version}, tex(mdbchr8c.vf) = %{tl_version}
Provides:       tex(mdbchr8t.vf) = %{tl_version}, tex(mdbchrc8t.vf) = %{tl_version}
Provides:       tex(mdbchrfc8t.vf) = %{tl_version}, tex(mdbchri7m.vf) = %{tl_version}
Provides:       tex(mdbchri7t.vf) = %{tl_version}, tex(mdbchri8c.vf) = %{tl_version}
Provides:       tex(mdbchri8t.vf) = %{tl_version}, tex(mdbchrifc8t.vf) = %{tl_version}
Provides:       tex(mdbchrma.vf) = %{tl_version}, tex(mdbchrmb.vf) = %{tl_version}
Provides:       tex(mdbchro7t.vf) = %{tl_version}, tex(mdbchro8c.vf) = %{tl_version}
Provides:       tex(mdbchro8t.vf) = %{tl_version}, tex(mdbchrofc8t.vf) = %{tl_version}
Provides:       tex(mdgrbCb7m.vf) = %{tl_version}, tex(mdgrbCbi7m.vf) = %{tl_version}
Provides:       tex(mdgrbCr7m.vf) = %{tl_version}, tex(mdgrbCri7m.vf) = %{tl_version}
Provides:       tex(mdgrbb7m.vf) = %{tl_version}, tex(mdgrbbi7m.vf) = %{tl_version}
Provides:       tex(mdgrbr7m.vf) = %{tl_version}, tex(mdgrbri7m.vf) = %{tl_version}
Provides:       tex(mdgrdCb7m.vf) = %{tl_version}, tex(mdgrdCbi7m.vf) = %{tl_version}
Provides:       tex(mdgrdCri7m.vf) = %{tl_version}, tex(mdgrdb7m.vf) = %{tl_version}
Provides:       tex(mdgrdbi7m.vf) = %{tl_version}, tex(mdgrdr7m.vf) = %{tl_version}
Provides:       tex(mdgrdrC7m.vf) = %{tl_version}, tex(mdgrdri7m.vf) = %{tl_version}
Provides:       tex(mdicib7m.vf) = %{tl_version}, tex(mdicib7t.vf) = %{tl_version}
Provides:       tex(mdicib7v.vf) = %{tl_version}, tex(mdicib7y.vf) = %{tl_version}
Provides:       tex(mdicib8c.vf) = %{tl_version}, tex(mdicib8t.vf) = %{tl_version}
Provides:       tex(mdicibc8c.vf) = %{tl_version}, tex(mdicibc8t.vf) = %{tl_version}
Provides:       tex(mdicibfc8t.vf) = %{tl_version}, tex(mdicibi7m.vf) = %{tl_version}
Provides:       tex(mdicibi7t.vf) = %{tl_version}, tex(mdicibi8c.vf) = %{tl_version}
Provides:       tex(mdicibi8t.vf) = %{tl_version}, tex(mdicibic8c.vf) = %{tl_version}
Provides:       tex(mdicibic8t.vf) = %{tl_version}, tex(mdicibifc8t.vf) = %{tl_version}
Provides:       tex(mdicibiu7m.vf) = %{tl_version}, tex(mdicibma.vf) = %{tl_version}
Provides:       tex(mdicibmb.vf) = %{tl_version}, tex(mdicibui7m.vf) = %{tl_version}
Provides:       tex(mdicic8c.vf) = %{tl_version}, tex(mdicic8t.vf) = %{tl_version}
Provides:       tex(mdicicc8c.vf) = %{tl_version}, tex(mdicicc8t.vf) = %{tl_version}
Provides:       tex(mdicicfc8t.vf) = %{tl_version}, tex(mdicici8c.vf) = %{tl_version}
Provides:       tex(mdicici8t.vf) = %{tl_version}, tex(mdicicic8c.vf) = %{tl_version}
Provides:       tex(mdicicic8t.vf) = %{tl_version}, tex(mdicicifc8t.vf) = %{tl_version}
Provides:       tex(mdicir7m.vf) = %{tl_version}, tex(mdicir7t.vf) = %{tl_version}
Provides:       tex(mdicir7v.vf) = %{tl_version}, tex(mdicir7y.vf) = %{tl_version}
Provides:       tex(mdicir8c.vf) = %{tl_version}, tex(mdicir8t.vf) = %{tl_version}
Provides:       tex(mdicirc8c.vf) = %{tl_version}, tex(mdicirc8t.vf) = %{tl_version}
Provides:       tex(mdicirfc8t.vf) = %{tl_version}, tex(mdiciri7m.vf) = %{tl_version}
Provides:       tex(mdiciri7t.vf) = %{tl_version}, tex(mdiciri8c.vf) = %{tl_version}
Provides:       tex(mdiciri8t.vf) = %{tl_version}, tex(mdiciric8c.vf) = %{tl_version}
Provides:       tex(mdiciric8t.vf) = %{tl_version}, tex(mdicirifc8t.vf) = %{tl_version}
Provides:       tex(mdiciriu7m.vf) = %{tl_version}, tex(mdicirma.vf) = %{tl_version}
Provides:       tex(mdicirmb.vf) = %{tl_version}, tex(mdicirui7m.vf) = %{tl_version}
Provides:       tex(mdxcib7y.vf) = %{tl_version}, tex(mdxcib8t.vf) = %{tl_version}
Provides:       tex(mdxcibc8t.vf) = %{tl_version}, tex(mdxcibi7y.vf) = %{tl_version}
Provides:       tex(mdxcibi8t.vf) = %{tl_version}, tex(mdxcibic8t.vf) = %{tl_version}
Provides:       tex(mdxcic7y.vf) = %{tl_version}, tex(mdxcic8t.vf) = %{tl_version}
Provides:       tex(mdxcicc8t.vf) = %{tl_version}, tex(mdxcici7y.vf) = %{tl_version}
Provides:       tex(mdxcici8t.vf) = %{tl_version}, tex(mdxcicic8t.vf) = %{tl_version}
Provides:       tex(mdxcir7y.vf) = %{tl_version}, tex(mdxcir8t.vf) = %{tl_version}
Provides:       tex(mdxcirc8t.vf) = %{tl_version}, tex(mdxciri7y.vf) = %{tl_version}
Provides:       tex(mdxciri8t.vf) = %{tl_version}, tex(mdxciric8t.vf) = %{tl_version}
Provides:       tex(mdpgdb8c.vf) = %{tl_version}, tex(mdpgdb8t.vf) = %{tl_version}
Provides:       tex(mdpgdbc8c.vf) = %{tl_version}, tex(mdpgdbc8t.vf) = %{tl_version}
Provides:       tex(mdpgdbfc8t.vf) = %{tl_version}, tex(mdpgdbi8c.vf) = %{tl_version}
Provides:       tex(mdpgdbi8t.vf) = %{tl_version}, tex(mdpgdbic8c.vf) = %{tl_version}
Provides:       tex(mdpgdbic8t.vf) = %{tl_version}, tex(mdpgdbifc8t.vf) = %{tl_version}
Provides:       tex(mdpgdr7m.vf) = %{tl_version}, tex(mdpgdr7t.vf) = %{tl_version}
Provides:       tex(mdpgdr7v.vf) = %{tl_version}, tex(mdpgdr7y.vf) = %{tl_version}
Provides:       tex(mdpgdr8c.vf) = %{tl_version}, tex(mdpgdr8t.vf) = %{tl_version}
Provides:       tex(mdpgdrc8c.vf) = %{tl_version}, tex(mdpgdrc8t.vf) = %{tl_version}
Provides:       tex(mdpgdrfc8t.vf) = %{tl_version}, tex(mdpgdri7m.vf) = %{tl_version}
Provides:       tex(mdpgdri7t.vf) = %{tl_version}, tex(mdpgdri8c.vf) = %{tl_version}
Provides:       tex(mdpgdri8t.vf) = %{tl_version}, tex(mdpgdric8c.vf) = %{tl_version}
Provides:       tex(mdpgdric8t.vf) = %{tl_version}, tex(mdpgdrifc8t.vf) = %{tl_version}
Provides:       tex(mdpgdrma.vf) = %{tl_version}, tex(mdpgdrmb.vf) = %{tl_version}
Provides:       tex(mdpgds7m.vf) = %{tl_version}, tex(mdpgds7t.vf) = %{tl_version}
Provides:       tex(mdpgds7v.vf) = %{tl_version}, tex(mdpgds7y.vf) = %{tl_version}
Provides:       tex(mdpgds8c.vf) = %{tl_version}, tex(mdpgds8t.vf) = %{tl_version}
Provides:       tex(mdpgdsc8c.vf) = %{tl_version}, tex(mdpgdsc8t.vf) = %{tl_version}
Provides:       tex(mdpgdsfc8t.vf) = %{tl_version}, tex(mdpgdsi7m.vf) = %{tl_version}
Provides:       tex(mdpgdsi7t.vf) = %{tl_version}, tex(mdpgdsi8c.vf) = %{tl_version}
Provides:       tex(mdpgdsi8t.vf) = %{tl_version}, tex(mdpgdsic8c.vf) = %{tl_version}
Provides:       tex(mdpgdsic8t.vf) = %{tl_version}, tex(mdpgdsifc8t.vf) = %{tl_version}
Provides:       tex(mdpgdsma.vf) = %{tl_version}, tex(mdpgdsmb.vf) = %{tl_version}
Provides:       tex(mdxgdb7y.vf) = %{tl_version}, tex(mdxgdb8t.vf) = %{tl_version}
Provides:       tex(mdxgdbc8t.vf) = %{tl_version}, tex(mdxgdbi7y.vf) = %{tl_version}
Provides:       tex(mdxgdbi8t.vf) = %{tl_version}, tex(mdxgdbic8t.vf) = %{tl_version}
Provides:       tex(mdxgdr7y.vf) = %{tl_version}, tex(mdxgdr8t.vf) = %{tl_version}
Provides:       tex(mdxgdrc8t.vf) = %{tl_version}, tex(mdxgdri7y.vf) = %{tl_version}
Provides:       tex(mdxgdri8t.vf) = %{tl_version}, tex(mdxgdric8t.vf) = %{tl_version}
Provides:       tex(mdxgds7y.vf) = %{tl_version}, tex(mdxgds8t.vf) = %{tl_version}
Provides:       tex(mdxgdsc8t.vf) = %{tl_version}, tex(mdxgdsi7y.vf) = %{tl_version}
Provides:       tex(mdxgdsi8t.vf) = %{tl_version}, tex(mdxgdsic8t.vf) = %{tl_version}
Provides:       tex(mdpusb8c.vf) = %{tl_version}, tex(mdpusb8t.vf) = %{tl_version}
Provides:       tex(mdpusbc8c.vf) = %{tl_version}, tex(mdpusbc8t.vf) = %{tl_version}
Provides:       tex(mdpusbfc8t.vf) = %{tl_version}, tex(mdpusbi8c.vf) = %{tl_version}
Provides:       tex(mdpusbi8t.vf) = %{tl_version}, tex(mdpusbic8c.vf) = %{tl_version}
Provides:       tex(mdpusbic8t.vf) = %{tl_version}, tex(mdpusbifc8t.vf) = %{tl_version}
Provides:       tex(mdpusr7m.vf) = %{tl_version}, tex(mdpusr7t.vf) = %{tl_version}
Provides:       tex(mdpusr7v.vf) = %{tl_version}, tex(mdpusr7y.vf) = %{tl_version}
Provides:       tex(mdpusr8c.vf) = %{tl_version}, tex(mdpusr8t.vf) = %{tl_version}
Provides:       tex(mdpusrc8c.vf) = %{tl_version}, tex(mdpusrc8t.vf) = %{tl_version}
Provides:       tex(mdpusrfc8t.vf) = %{tl_version}, tex(mdpusri7m.vf) = %{tl_version}
Provides:       tex(mdpusri7t.vf) = %{tl_version}, tex(mdpusri8c.vf) = %{tl_version}
Provides:       tex(mdpusri8t.vf) = %{tl_version}, tex(mdpusric8c.vf) = %{tl_version}
Provides:       tex(mdpusric8t.vf) = %{tl_version}, tex(mdpusrifc8t.vf) = %{tl_version}
Provides:       tex(mdpusrma.vf) = %{tl_version}, tex(mdpusrmb.vf) = %{tl_version}
Provides:       tex(mdpuss7m.vf) = %{tl_version}, tex(mdpuss7t.vf) = %{tl_version}
Provides:       tex(mdpuss7v.vf) = %{tl_version}, tex(mdpuss7y.vf) = %{tl_version}
Provides:       tex(mdpuss8c.vf) = %{tl_version}, tex(mdpuss8t.vf) = %{tl_version}
Provides:       tex(mdpussc8c.vf) = %{tl_version}, tex(mdpussc8t.vf) = %{tl_version}
Provides:       tex(mdpussfc8t.vf) = %{tl_version}, tex(mdpussi7m.vf) = %{tl_version}
Provides:       tex(mdpussi7t.vf) = %{tl_version}, tex(mdpussi8c.vf) = %{tl_version}
Provides:       tex(mdpussi8t.vf) = %{tl_version}, tex(mdpussic8c.vf) = %{tl_version}
Provides:       tex(mdpussic8t.vf) = %{tl_version}, tex(mdpussifc8t.vf) = %{tl_version}
Provides:       tex(mdpussma.vf) = %{tl_version}, tex(mdpussmb.vf) = %{tl_version}
Provides:       tex(mdxusb7y.vf) = %{tl_version}, tex(mdxusb8t.vf) = %{tl_version}
Provides:       tex(mdxusbc8t.vf) = %{tl_version}, tex(mdxusbi7y.vf) = %{tl_version}
Provides:       tex(mdxusbi8t.vf) = %{tl_version}, tex(mdxusbic8t.vf) = %{tl_version}
Provides:       tex(mdxusr7y.vf) = %{tl_version}, tex(mdxusr8t.vf) = %{tl_version}
Provides:       tex(mdxusrc8t.vf) = %{tl_version}, tex(mdxusri7y.vf) = %{tl_version}
Provides:       tex(mdxusri8t.vf) = %{tl_version}, tex(mdxusric8t.vf) = %{tl_version}
Provides:       tex(mdxuss7y.vf) = %{tl_version}, tex(mdxuss8t.vf) = %{tl_version}
Provides:       tex(mdxussc8t.vf) = %{tl_version}, tex(mdxussi7y.vf) = %{tl_version}
Provides:       tex(mdxussi8t.vf) = %{tl_version}, tex(mdxussic8t.vf) = %{tl_version}
Provides:       tex(mdputb7m.vf) = %{tl_version}, tex(mdputb7t.vf) = %{tl_version}
Provides:       tex(mdputb7v.vf) = %{tl_version}, tex(mdputb7y.vf) = %{tl_version}
Provides:       tex(mdputb8c.vf) = %{tl_version}, tex(mdputb8t.vf) = %{tl_version}
Provides:       tex(mdputbc8t.vf) = %{tl_version}, tex(mdputbfc8t.vf) = %{tl_version}
Provides:       tex(mdputbi7m.vf) = %{tl_version}, tex(mdputbi7t.vf) = %{tl_version}
Provides:       tex(mdputbi8c.vf) = %{tl_version}, tex(mdputbi8t.vf) = %{tl_version}
Provides:       tex(mdputbifc8t.vf) = %{tl_version}, tex(mdputbma.vf) = %{tl_version}
Provides:       tex(mdputbmb.vf) = %{tl_version}, tex(mdputbo7t.vf) = %{tl_version}
Provides:       tex(mdputbo8c.vf) = %{tl_version}, tex(mdputbo8t.vf) = %{tl_version}
Provides:       tex(mdputbofc8t.vf) = %{tl_version}, tex(mdputr7m.vf) = %{tl_version}
Provides:       tex(mdputr7t.vf) = %{tl_version}, tex(mdputr7v.vf) = %{tl_version}
Provides:       tex(mdputr7y.vf) = %{tl_version}, tex(mdputr8c.vf) = %{tl_version}
Provides:       tex(mdputr8t.vf) = %{tl_version}, tex(mdputrc8t.vf) = %{tl_version}
Provides:       tex(mdputrfc8t.vf) = %{tl_version}, tex(mdputri7m.vf) = %{tl_version}
Provides:       tex(mdputri7t.vf) = %{tl_version}, tex(mdputri8c.vf) = %{tl_version}
Provides:       tex(mdputri8t.vf) = %{tl_version}, tex(mdputrifc8t.vf) = %{tl_version}
Provides:       tex(mdputrma.vf) = %{tl_version}, tex(mdputrmb.vf) = %{tl_version}
Provides:       tex(mdputro7t.vf) = %{tl_version}, tex(mdputro8c.vf) = %{tl_version}
Provides:       tex(mdputro8t.vf) = %{tl_version}, tex(mdputrofc8t.vf) = %{tl_version}
Provides:       tex(mdugmm7m.vf) = %{tl_version}, tex(mdugmm7t.vf) = %{tl_version}
Provides:       tex(mdugmm7v.vf) = %{tl_version}, tex(mdugmm7y.vf) = %{tl_version}
Provides:       tex(mdugmm8c.vf) = %{tl_version}, tex(mdugmm8t.vf) = %{tl_version}
Provides:       tex(mdugmmfc8t.vf) = %{tl_version}, tex(mdugmmi7m.vf) = %{tl_version}
Provides:       tex(mdugmmi7t.vf) = %{tl_version}, tex(mdugmmi8c.vf) = %{tl_version}
Provides:       tex(mdugmmi8t.vf) = %{tl_version}, tex(mdugmmifc8t.vf) = %{tl_version}
Provides:       tex(mdugmmma.vf) = %{tl_version}, tex(mdugmmmb.vf) = %{tl_version}
Provides:       tex(mdugmmo7t.vf) = %{tl_version}, tex(mdugmmo8c.vf) = %{tl_version}
Provides:       tex(mdugmmo8t.vf) = %{tl_version}, tex(mdugmmofc8t.vf) = %{tl_version}
Provides:       tex(mdugmr7m.vf) = %{tl_version}, tex(mdugmr7t.vf) = %{tl_version}
Provides:       tex(mdugmr7v.vf) = %{tl_version}, tex(mdugmr7y.vf) = %{tl_version}
Provides:       tex(mdugmr8c.vf) = %{tl_version}, tex(mdugmr8t.vf) = %{tl_version}
Provides:       tex(mdugmrfc8t.vf) = %{tl_version}, tex(mdugmri7m.vf) = %{tl_version}
Provides:       tex(mdugmri7t.vf) = %{tl_version}, tex(mdugmri8c.vf) = %{tl_version}
Provides:       tex(mdugmri8t.vf) = %{tl_version}, tex(mdugmrifc8t.vf) = %{tl_version}
Provides:       tex(mdugmrma.vf) = %{tl_version}, tex(mdugmrmb.vf) = %{tl_version}
Provides:       tex(mdugmro7t.vf) = %{tl_version}, tex(mdugmro8c.vf) = %{tl_version}
Provides:       tex(mdugmro8t.vf) = %{tl_version}, tex(mdugmrofc8t.vf) = %{tl_version}
Provides:       tex(mathdesign.sty) = %{tl_version}, tex(mdacmr.fd) = %{tl_version}
Provides:       tex(mdamdbch.fd) = %{tl_version}, tex(mdbch.cfg) = %{tl_version}
Provides:       tex(mdbch.sty) = %{tl_version}, tex(mdbmdbch.fd) = %{tl_version}
Provides:       tex(omlmdbch.fd) = %{tl_version}, tex(omsmdbch.fd) = %{tl_version}
Provides:       tex(omxmdbch.fd) = %{tl_version}, tex(ot1mdbch.fd) = %{tl_version}
Provides:       tex(t1mdbch.fd) = %{tl_version}, tex(ts1mdbch.fd) = %{tl_version}
Provides:       tex(mdbcmr.fd) = %{tl_version}, tex(mdfont.def) = %{tl_version}
Provides:       tex(mdamdici.fd) = %{tl_version}, tex(mdbmdici.fd) = %{tl_version}
Provides:       tex(mdici.cfg) = %{tl_version}, tex(mdici.sty) = %{tl_version}
Provides:       tex(omlmdici.fd) = %{tl_version}, tex(omsmdici.fd) = %{tl_version}
Provides:       tex(omxmdici.fd) = %{tl_version}, tex(ot1mdici.fd) = %{tl_version}
Provides:       tex(t1mdici.fd) = %{tl_version}, tex(ts1mdici.fd) = %{tl_version}
Provides:       tex(mdamdpgd.fd) = %{tl_version}, tex(mdbmdpgd.fd) = %{tl_version}
Provides:       tex(mdpgd.cfg) = %{tl_version}, tex(mdpgd.sty) = %{tl_version}
Provides:       tex(omlmdpgd.fd) = %{tl_version}, tex(omsmdpgd.fd) = %{tl_version}
Provides:       tex(omxmdpgd.fd) = %{tl_version}, tex(ot1mdpgd.fd) = %{tl_version}
Provides:       tex(t1mdpgd.fd) = %{tl_version}, tex(ts1mdpgd.fd) = %{tl_version}
Provides:       tex(mdamdpus.fd) = %{tl_version}, tex(mdbmdpus.fd) = %{tl_version}
Provides:       tex(mdpus.cfg) = %{tl_version}, tex(mdpus.sty) = %{tl_version}
Provides:       tex(omlmdpus.fd) = %{tl_version}, tex(omsmdpus.fd) = %{tl_version}
Provides:       tex(omxmdpus.fd) = %{tl_version}, tex(ot1mdpus.fd) = %{tl_version}
Provides:       tex(t1mdpus.fd) = %{tl_version}, tex(ts1mdpus.fd) = %{tl_version}
Provides:       tex(mdamdput.fd) = %{tl_version}, tex(mdbmdput.fd) = %{tl_version}
Provides:       tex(mdput.cfg) = %{tl_version}, tex(mdput.sty) = %{tl_version}
Provides:       tex(omlmdput.fd) = %{tl_version}, tex(omsmdput.fd) = %{tl_version}
Provides:       tex(omxmdput.fd) = %{tl_version}, tex(ot1mdput.fd) = %{tl_version}
Provides:       tex(t1mdput.fd) = %{tl_version}, tex(ts1mdput.fd) = %{tl_version}
Provides:       tex(mdsffont.def) = %{tl_version}, tex(mdttfont.def) = %{tl_version}
Provides:       tex(mdamdugm.fd) = %{tl_version}, tex(mdbmdugm.fd) = %{tl_version}
Provides:       tex(mdugm.cfg) = %{tl_version}, tex(mdugm.sty) = %{tl_version}
Provides:       tex(omlmdugm.fd) = %{tl_version}, tex(omsmdugm.fd) = %{tl_version}
Provides:       tex(omxmdugm.fd) = %{tl_version}, tex(ot1mdugm.fd) = %{tl_version}
Provides:       tex(t1mdugm.fd) = %{tl_version}, tex(ts1mdugm.fd) = %{tl_version}
Provides:       tex(omlmdgrb.fd) = %{tl_version}, tex(omlmdgrbc.fd) = %{tl_version}
Provides:       tex(omlmdgrd.fd) = %{tl_version}, tex(omlmdgrdc.fd) = %{tl_version}

%description -n texlive-mathdesign
The Math Design project offers free mathematical fonts that
match with existing text fonts. To date, three free font
families are available: Adobe Utopia, URW Garamond and
Bitstream Charter. Three commercial fonts are also supported:
Adobe Garamond Pro, Adobe UtopiaStd and ITC Charter. Mathdesign
covers the whole LaTeX glyph set, including AMS symbols and
some extra. Both roman and bold versions of these symbols can
be used. Moreover you can choose between three greek fonts (two
of them created by the Greek Font Society).

%package -n texlive-mathdesign-doc
Summary:        Documentation for mathdesign
Version:        svn31639.2.31

Provides:       tex-mathdesign-doc
AutoReqProv:    No

%description -n texlive-mathdesign-doc
Documentation for mathdesign

%package -n texlive-mdputu
Provides:       tex-mdputu = %{tl_version}
License:        BSD
Summary:        Upright digits in Adobe Utopia Italic
Version:        svn20298.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mdputubi7t.tfm) = %{tl_version}, tex(mdputubi8t.tfm) = %{tl_version}
Provides:       tex(mdputuri7t.tfm) = %{tl_version}, tex(mdputuri8t.tfm) = %{tl_version}
Provides:       tex(mdputubi7t.vf) = %{tl_version}, tex(mdputubi8t.vf) = %{tl_version}
Provides:       tex(mdputuri7t.vf) = %{tl_version}, tex(mdputuri8t.vf) = %{tl_version}
Provides:       tex(mdputu.sty) = %{tl_version}, tex(ot1mdputu.fd) = %{tl_version}
Provides:       tex(t1mdputu.fd) = %{tl_version}

%description -n texlive-mdputu
The Annals of Mathematics uses italics for theorems. However,
slanted digits and parentheses look disturbing when surrounded
by (upright) mathematics. This package provides virtual fonts
with italics and upright digits and punctuation, as an
extension to Mathdesign's Utopia bundle.

%package -n texlive-mdputu-doc
Summary:        Documentation for mdputu
Version:        svn20298.1.2

Provides:       tex-mdputu-doc
AutoReqProv:    No

%description -n texlive-mdputu-doc
Documentation for mdputu

%package -n texlive-mdsymbol
Provides:       tex-mdsymbol = %{tl_version}
License:        OFL
Summary:        Symbol fonts to match Adobe Myriad Pro
Version:        svn28399.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty), tex(amsmath.sty), tex(textcomp.sty), tex(etoolbox.sty)
Requires:       tex(fltpoint.sty), tex(calc.sty)
Provides:       tex(mdsymbol-a.enc) = %{tl_version}, tex(mdsymbol-b.enc) = %{tl_version}
Provides:       tex(mdsymbol-c.enc) = %{tl_version}, tex(mdsymbol-d.enc) = %{tl_version}
Provides:       tex(mdsymbol-e.enc) = %{tl_version}, tex(mdsymbol-f.enc) = %{tl_version}
Provides:       tex(mdsymbol.map) = %{tl_version}, tex(MdSymbol-Bold.otf) = %{tl_version}
Provides:       tex(MdSymbol-Light.otf) = %{tl_version}, tex(MdSymbol-Regular.otf) = %{tl_version}
Provides:       tex(MdSymbol-Semibold.otf) = %{tl_version}
Provides:       tex(MdSymbolA-Bold.tfm) = %{tl_version}, tex(MdSymbolA-Light.tfm) = %{tl_version}
Provides:       tex(MdSymbolA-Regular.tfm) = %{tl_version}
Provides:       tex(MdSymbolA-Semibold.tfm) = %{tl_version}
Provides:       tex(MdSymbolB-Bold.tfm) = %{tl_version}, tex(MdSymbolB-Light.tfm) = %{tl_version}
Provides:       tex(MdSymbolB-Regular.tfm) = %{tl_version}
Provides:       tex(MdSymbolB-Semibold.tfm) = %{tl_version}
Provides:       tex(MdSymbolC-Bold.tfm) = %{tl_version}, tex(MdSymbolC-Light.tfm) = %{tl_version}
Provides:       tex(MdSymbolC-Regular.tfm) = %{tl_version}
Provides:       tex(MdSymbolC-Semibold.tfm) = %{tl_version}
Provides:       tex(MdSymbolD-Bold.tfm) = %{tl_version}, tex(MdSymbolD-Light.tfm) = %{tl_version}
Provides:       tex(MdSymbolD-Regular.tfm) = %{tl_version}
Provides:       tex(MdSymbolD-Semibold.tfm) = %{tl_version}
Provides:       tex(MdSymbolE-Bold.tfm) = %{tl_version}, tex(MdSymbolE-Light.tfm) = %{tl_version}
Provides:       tex(MdSymbolE-Regular.tfm) = %{tl_version}
Provides:       tex(MdSymbolE-Semibold.tfm) = %{tl_version}
Provides:       tex(MdSymbolF-Bold.tfm) = %{tl_version}, tex(MdSymbolF-Light.tfm) = %{tl_version}
Provides:       tex(MdSymbolF-Regular.tfm) = %{tl_version}
Provides:       tex(MdSymbolF-Semibold.tfm) = %{tl_version}
Provides:       tex(MdSymbolA-Bold.pfb) = %{tl_version}, tex(MdSymbolA-Light.pfb) = %{tl_version}
Provides:       tex(MdSymbolA-Regular.pfb) = %{tl_version}
Provides:       tex(MdSymbolA-Semibold.pfb) = %{tl_version}
Provides:       tex(MdSymbolB-Bold.pfb) = %{tl_version}, tex(MdSymbolB-Light.pfb) = %{tl_version}
Provides:       tex(MdSymbolB-Regular.pfb) = %{tl_version}
Provides:       tex(MdSymbolB-Semibold.pfb) = %{tl_version}
Provides:       tex(MdSymbolC-Bold.pfb) = %{tl_version}, tex(MdSymbolC-Light.pfb) = %{tl_version}
Provides:       tex(MdSymbolC-Regular.pfb) = %{tl_version}
Provides:       tex(MdSymbolC-Semibold.pfb) = %{tl_version}
Provides:       tex(MdSymbolD-Bold.pfb) = %{tl_version}, tex(MdSymbolD-Light.pfb) = %{tl_version}
Provides:       tex(MdSymbolD-Regular.pfb) = %{tl_version}
Provides:       tex(MdSymbolD-Semibold.pfb) = %{tl_version}
Provides:       tex(MdSymbolE-Bold.pfb) = %{tl_version}, tex(MdSymbolE-Light.pfb) = %{tl_version}
Provides:       tex(MdSymbolE-Regular.pfb) = %{tl_version}
Provides:       tex(MdSymbolE-Semibold.pfb) = %{tl_version}
Provides:       tex(MdSymbolF-Bold.pfb) = %{tl_version}, tex(MdSymbolF-Light.pfb) = %{tl_version}
Provides:       tex(MdSymbolF-Regular.pfb) = %{tl_version}
Provides:       tex(MdSymbolF-Semibold.pfb) = %{tl_version}
Provides:       tex(mdsymbol.sty) = %{tl_version}

%description -n texlive-mdsymbol
The package provides a font of mathematical symbols, MyriadPro
The font is designed as a companion to Adobe Myriad Pro, but it
might also fit well with other contemporary typefaces.

%package -n texlive-mdsymbol-doc
Summary:        Documentation for mdsymbol
Version:        svn28399.0.5

Provides:       tex-mdsymbol-doc
AutoReqProv:    No

%description -n texlive-mdsymbol-doc
Documentation for mdsymbol

%package -n texlive-merriweather
Provides:       tex-merriweather = %{tl_version}
License:        OFL
Summary:        Merriweather and MerriweatherSans fonts, with LaTeX support
Version:        svn34315.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(textcomp.sty), tex(xkeyval.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty), tex(mweights.sty)
Provides:       tex(mwth_5q2vgd.enc) = %{tl_version}, tex(mwth_cn5sfl.enc) = %{tl_version}
Provides:       tex(mwth_fuknsh.enc) = %{tl_version}, tex(mwth_jnnjab.enc) = %{tl_version}
Provides:       tex(mwth_libw2m.enc) = %{tl_version}, tex(mwth_lnkfbl.enc) = %{tl_version}
Provides:       tex(mwth_oaf34p.enc) = %{tl_version}, tex(mwth_xz5wux.enc) = %{tl_version}
Provides:       tex(mwth_ywgpba.enc) = %{tl_version}, tex(mwth_z4e4wk.enc) = %{tl_version}
Provides:       tex(merriweather.map) = %{tl_version}, tex(Merriweather-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Merriweather-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Merriweather-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Merriweather-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Merriweather-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Light-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Light-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Light-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-Light-osf-t1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Light-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-Light-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Merriweather-LightIt-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Merriweather-LightIt-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Merriweather-LightIt-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-LightIt-osf-t1.tfm) = %{tl_version}
Provides:       tex(Merriweather-LightIt-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-LightIt-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBdIt-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBdIt-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBdIt-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBdIt-osf-t1.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBdIt-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBdIt-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBold-osf-t1.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Merriweather-UltraBold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MerriweatherSans-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Merriweather-Bold.ttf) = %{tl_version}
Provides:       tex(Merriweather-BoldIt.ttf) = %{tl_version}
Provides:       tex(Merriweather-Italic.ttf) = %{tl_version}
Provides:       tex(Merriweather-Light.ttf) = %{tl_version}
Provides:       tex(Merriweather-LightIt.ttf) = %{tl_version}
Provides:       tex(Merriweather-Regular.ttf) = %{tl_version}
Provides:       tex(Merriweather-UltraBdIt.ttf) = %{tl_version}
Provides:       tex(Merriweather-UltraBold.ttf) = %{tl_version}
Provides:       tex(MerriweatherSans-Bold.ttf) = %{tl_version}
Provides:       tex(MerriweatherSans-BoldItalic.ttf) = %{tl_version}
Provides:       tex(MerriweatherSans-ExBoldIt.ttf) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBold.ttf) = %{tl_version}
Provides:       tex(MerriweatherSans-Italic.ttf) = %{tl_version}
Provides:       tex(MerriweatherSans-Light.ttf) = %{tl_version}
Provides:       tex(MerriweatherSans-LightItalic.ttf) = %{tl_version}
Provides:       tex(MerriweatherSans-Regular.ttf) = %{tl_version}
Provides:       tex(Merriweather-Bold.pfb) = %{tl_version}
Provides:       tex(Merriweather-BoldIt.pfb) = %{tl_version}
Provides:       tex(Merriweather-Italic.pfb) = %{tl_version}
Provides:       tex(Merriweather-Light.pfb) = %{tl_version}
Provides:       tex(Merriweather-LightIt.pfb) = %{tl_version}
Provides:       tex(Merriweather-Regular.pfb) = %{tl_version}
Provides:       tex(Merriweather-UltraBdIt.pfb) = %{tl_version}
Provides:       tex(Merriweather-UltraBold.pfb) = %{tl_version}
Provides:       tex(MerriweatherSans-Bold.pfb) = %{tl_version}
Provides:       tex(MerriweatherSans-BoldItalic.pfb) = %{tl_version}
Provides:       tex(MerriweatherSans-ExBoldIt.pfb) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBold.pfb) = %{tl_version}
Provides:       tex(MerriweatherSans-Italic.pfb) = %{tl_version}
Provides:       tex(MerriweatherSans-Light.pfb) = %{tl_version}
Provides:       tex(MerriweatherSans-LightItalic.pfb) = %{tl_version}
Provides:       tex(MerriweatherSans-Regular.pfb) = %{tl_version}
Provides:       tex(Merriweather-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(Merriweather-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(Merriweather-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Merriweather-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Merriweather-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(Merriweather-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Merriweather-Light-osf-t1.vf) = %{tl_version}
Provides:       tex(Merriweather-Light-osf-ts1.vf) = %{tl_version}
Provides:       tex(Merriweather-LightIt-osf-t1.vf) = %{tl_version}
Provides:       tex(Merriweather-LightIt-osf-ts1.vf) = %{tl_version}
Provides:       tex(Merriweather-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(Merriweather-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(Merriweather-UltraBdIt-osf-t1.vf) = %{tl_version}
Provides:       tex(Merriweather-UltraBdIt-osf-ts1.vf) = %{tl_version}
Provides:       tex(Merriweather-UltraBold-osf-t1.vf) = %{tl_version}
Provides:       tex(Merriweather-UltraBold-osf-ts1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-ExtraBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(MerriweatherSans-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Merriweather-OsF.fd) = %{tl_version}
Provides:       tex(LY1MerriweatherSans-TLF.fd) = %{tl_version}
Provides:       tex(OT1Merriweather-OsF.fd) = %{tl_version}
Provides:       tex(OT1MerriweatherSans-TLF.fd) = %{tl_version}
Provides:       tex(T1Merriweather-OsF.fd) = %{tl_version}
Provides:       tex(T1MerriweatherSans-TLF.fd) = %{tl_version}
Provides:       tex(TS1Merriweather-OsF.fd) = %{tl_version}
Provides:       tex(TS1MerriweatherSans-TLF.fd) = %{tl_version}
Provides:       tex(merriweather.sty) = %{tl_version}

%description -n texlive-merriweather
Merriweather features a very large x height, slightly condensed
letterforms, a mild diagonal stress, sturdy serifs and open
forms. The Sans family closely harmonizes with the weights and
styles of the serif family. There are four weights and italics
for each.

%package -n texlive-merriweather-doc
Summary:        Documentation for merriweather
Version:        svn34315.0

Provides:       tex-merriweather-doc
AutoReqProv:    No

%description -n texlive-merriweather-doc
Documentation for merriweather

%package -n texlive-mintspirit
Provides:       tex-mintspirit = %{tl_version}
License:        OFL
Summary:        LaTeX support for MintSpirit font families
Version:        svn32069.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(textcomp.sty), tex(xkeyval.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty)
Provides:       tex(mntsprt2_24uybq.enc) = %{tl_version}
Provides:       tex(mntsprt2_2dxuba.enc) = %{tl_version}
Provides:       tex(mntsprt2_3vy5j3.enc) = %{tl_version}
Provides:       tex(mntsprt2_5cazkt.enc) = %{tl_version}
Provides:       tex(mntsprt2_63vcua.enc) = %{tl_version}
Provides:       tex(mntsprt2_6x4rw3.enc) = %{tl_version}
Provides:       tex(mntsprt2_7ayy44.enc) = %{tl_version}
Provides:       tex(mntsprt2_7u5374.enc) = %{tl_version}
Provides:       tex(mntsprt2_amdskp.enc) = %{tl_version}
Provides:       tex(mntsprt2_biiinc.enc) = %{tl_version}
Provides:       tex(mntsprt2_bkoczj.enc) = %{tl_version}
Provides:       tex(mntsprt2_dnk3mn.enc) = %{tl_version}
Provides:       tex(mntsprt2_eex3ia.enc) = %{tl_version}
Provides:       tex(mntsprt2_eqihrw.enc) = %{tl_version}
Provides:       tex(mntsprt2_eqrkmo.enc) = %{tl_version}
Provides:       tex(mntsprt2_fizmng.enc) = %{tl_version}
Provides:       tex(mntsprt2_fm3wlu.enc) = %{tl_version}
Provides:       tex(mntsprt2_j4bodc.enc) = %{tl_version}
Provides:       tex(mntsprt2_k4fv75.enc) = %{tl_version}
Provides:       tex(mntsprt2_l3e5vj.enc) = %{tl_version}
Provides:       tex(mntsprt2_lm7mhw.enc) = %{tl_version}
Provides:       tex(mntsprt2_lwraz3.enc) = %{tl_version}
Provides:       tex(mntsprt2_me5dp6.enc) = %{tl_version}
Provides:       tex(mntsprt2_oe76kg.enc) = %{tl_version}
Provides:       tex(mntsprt2_ref42g.enc) = %{tl_version}
Provides:       tex(mntsprt2_s7rd6p.enc) = %{tl_version}
Provides:       tex(mntsprt2_taixll.enc) = %{tl_version}
Provides:       tex(mntsprt2_tmtdfz.enc) = %{tl_version}
Provides:       tex(mntsprt2_ywkmiw.enc) = %{tl_version}
Provides:       tex(mntsprt_2isll4.enc) = %{tl_version}, tex(mntsprt_3sm7wd.enc) = %{tl_version}
Provides:       tex(mntsprt_3y5hmb.enc) = %{tl_version}, tex(mntsprt_5lbatd.enc) = %{tl_version}
Provides:       tex(mntsprt_5yvi6n.enc) = %{tl_version}, tex(mntsprt_675dmr.enc) = %{tl_version}
Provides:       tex(mntsprt_7enqs3.enc) = %{tl_version}, tex(mntsprt_bjjcsi.enc) = %{tl_version}
Provides:       tex(mntsprt_f4utek.enc) = %{tl_version}, tex(mntsprt_gcdgcc.enc) = %{tl_version}
Provides:       tex(mntsprt_gdx47l.enc) = %{tl_version}, tex(mntsprt_girsvq.enc) = %{tl_version}
Provides:       tex(mntsprt_gr6qqq.enc) = %{tl_version}, tex(mntsprt_imdxi4.enc) = %{tl_version}
Provides:       tex(mntsprt_lvhuc6.enc) = %{tl_version}, tex(mntsprt_lzc2o4.enc) = %{tl_version}
Provides:       tex(mntsprt_oj7rfe.enc) = %{tl_version}, tex(mntsprt_opresw.enc) = %{tl_version}
Provides:       tex(mntsprt_pulfbi.enc) = %{tl_version}, tex(mntsprt_swumq4.enc) = %{tl_version}
Provides:       tex(mntsprt_v6lq4b.enc) = %{tl_version}, tex(mntsprt_wk34ig.enc) = %{tl_version}
Provides:       tex(mntsprt_y4xqha.enc) = %{tl_version}, tex(mntsprt_zt2pqo.enc) = %{tl_version}
Provides:       tex(mintspirit.map) = %{tl_version}, tex(MintSpirit-Bold.otf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic.otf) = %{tl_version}
Provides:       tex(MintSpirit-Italic.otf) = %{tl_version}
Provides:       tex(MintSpirit-Regular.otf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold.otf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic.otf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic.otf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular.otf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MintSpirit-Bold.pfb) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic.pfb) = %{tl_version}
Provides:       tex(MintSpirit-Italic.pfb) = %{tl_version}
Provides:       tex(MintSpirit-Regular.pfb) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold.pfb) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic.pfb) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic.pfb) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular.pfb) = %{tl_version}
Provides:       tex(MintSpirit-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(MintSpirit-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(MintSpiritNo2-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LY1MintSpirit-Inf.fd) = %{tl_version}
Provides:       tex(LY1MintSpirit-LF.fd) = %{tl_version}
Provides:       tex(LY1MintSpirit-OsF.fd) = %{tl_version}
Provides:       tex(LY1MintSpirit-Sup.fd) = %{tl_version}
Provides:       tex(LY1MintSpirit-TLF.fd) = %{tl_version}
Provides:       tex(LY1MintSpirit-TOsF.fd) = %{tl_version}
Provides:       tex(LY1MintSpiritNoTwo-Inf.fd) = %{tl_version}
Provides:       tex(LY1MintSpiritNoTwo-LF.fd) = %{tl_version}
Provides:       tex(LY1MintSpiritNoTwo-OsF.fd) = %{tl_version}
Provides:       tex(LY1MintSpiritNoTwo-Sup.fd) = %{tl_version}
Provides:       tex(LY1MintSpiritNoTwo-TLF.fd) = %{tl_version}
Provides:       tex(LY1MintSpiritNoTwo-TOsF.fd) = %{tl_version}
Provides:       tex(OT1MintSpirit-Inf.fd) = %{tl_version}
Provides:       tex(OT1MintSpirit-LF.fd) = %{tl_version}
Provides:       tex(OT1MintSpirit-OsF.fd) = %{tl_version}
Provides:       tex(OT1MintSpirit-Sup.fd) = %{tl_version}
Provides:       tex(OT1MintSpirit-TLF.fd) = %{tl_version}
Provides:       tex(OT1MintSpirit-TOsF.fd) = %{tl_version}
Provides:       tex(OT1MintSpiritNoTwo-Inf.fd) = %{tl_version}
Provides:       tex(OT1MintSpiritNoTwo-LF.fd) = %{tl_version}
Provides:       tex(OT1MintSpiritNoTwo-OsF.fd) = %{tl_version}
Provides:       tex(OT1MintSpiritNoTwo-Sup.fd) = %{tl_version}
Provides:       tex(OT1MintSpiritNoTwo-TLF.fd) = %{tl_version}
Provides:       tex(OT1MintSpiritNoTwo-TOsF.fd) = %{tl_version}
Provides:       tex(T1MintSpirit-Inf.fd) = %{tl_version}
Provides:       tex(T1MintSpirit-LF.fd) = %{tl_version}, tex(T1MintSpirit-OsF.fd) = %{tl_version}
Provides:       tex(T1MintSpirit-Sup.fd) = %{tl_version}
Provides:       tex(T1MintSpirit-TLF.fd) = %{tl_version}
Provides:       tex(T1MintSpirit-TOsF.fd) = %{tl_version}
Provides:       tex(T1MintSpiritNoTwo-Inf.fd) = %{tl_version}
Provides:       tex(T1MintSpiritNoTwo-LF.fd) = %{tl_version}
Provides:       tex(T1MintSpiritNoTwo-OsF.fd) = %{tl_version}
Provides:       tex(T1MintSpiritNoTwo-Sup.fd) = %{tl_version}
Provides:       tex(T1MintSpiritNoTwo-TLF.fd) = %{tl_version}
Provides:       tex(T1MintSpiritNoTwo-TOsF.fd) = %{tl_version}
Provides:       tex(TS1MintSpirit-LF.fd) = %{tl_version}
Provides:       tex(TS1MintSpirit-OsF.fd) = %{tl_version}
Provides:       tex(TS1MintSpirit-TLF.fd) = %{tl_version}
Provides:       tex(TS1MintSpirit-TOsF.fd) = %{tl_version}
Provides:       tex(TS1MintSpiritNoTwo-LF.fd) = %{tl_version}
Provides:       tex(TS1MintSpiritNoTwo-OsF.fd) = %{tl_version}
Provides:       tex(TS1MintSpiritNoTwo-TLF.fd) = %{tl_version}
Provides:       tex(TS1MintSpiritNoTwo-TOsF.fd) = %{tl_version}
Provides:       tex(mintspirit.sty) = %{tl_version}, tex(mintspirit2.sty) = %{tl_version}

%description -n texlive-mintspirit
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the MintSpirit and MintSpiritNo2 families of fonts,
designed by Hirwen Harendal. MintSpirit was originally designed
for use as a system font on a Linux Mint system. The No. 2
variant provides more conventional shapes for some glyphs.

%package -n texlive-mintspirit-doc
Summary:        Documentation for mintspirit
Version:        svn32069.0

Provides:       tex-mintspirit-doc
AutoReqProv:    No

%description -n texlive-mintspirit-doc
Documentation for mintspirit

%package -n texlive-mnsymbol
Provides:       tex-mnsymbol = %{tl_version}
License:        Public Domain
Summary:        Mathematical symbol font for Adobe MinionPro
Version:        svn18651.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(textcomp.sty), tex(eufrak.sty), tex(amsmath.sty)
Provides:       tex(MnSymbolA.enc) = %{tl_version}, tex(MnSymbolB.enc) = %{tl_version}
Provides:       tex(MnSymbolC.enc) = %{tl_version}, tex(MnSymbolD.enc) = %{tl_version}
Provides:       tex(MnSymbolE.enc) = %{tl_version}, tex(MnSymbolF.enc) = %{tl_version}
Provides:       tex(MnSymbolS.enc) = %{tl_version}, tex(MnSymbol.map) = %{tl_version}
Provides:       tex(MnSymbol-Bold10.otf) = %{tl_version}
Provides:       tex(MnSymbol-Bold12.otf) = %{tl_version}
Provides:       tex(MnSymbol-Bold5.otf) = %{tl_version}, tex(MnSymbol-Bold6.otf) = %{tl_version}
Provides:       tex(MnSymbol-Bold7.otf) = %{tl_version}, tex(MnSymbol-Bold8.otf) = %{tl_version}
Provides:       tex(MnSymbol-Bold9.otf) = %{tl_version}, tex(MnSymbol10.otf) = %{tl_version}
Provides:       tex(MnSymbol12.otf) = %{tl_version}, tex(MnSymbol5.otf) = %{tl_version}
Provides:       tex(MnSymbol6.otf) = %{tl_version}, tex(MnSymbol7.otf) = %{tl_version}
Provides:       tex(MnSymbol8.otf) = %{tl_version}, tex(MnSymbol9.otf) = %{tl_version}
Provides:       tex(MnSymbolA-Bold10.tfm) = %{tl_version}
Provides:       tex(MnSymbolA-Bold12.tfm) = %{tl_version}
Provides:       tex(MnSymbolA-Bold5.tfm) = %{tl_version}
Provides:       tex(MnSymbolA-Bold6.tfm) = %{tl_version}
Provides:       tex(MnSymbolA-Bold7.tfm) = %{tl_version}
Provides:       tex(MnSymbolA-Bold8.tfm) = %{tl_version}
Provides:       tex(MnSymbolA-Bold9.tfm) = %{tl_version}
Provides:       tex(MnSymbolA10.tfm) = %{tl_version}, tex(MnSymbolA12.tfm) = %{tl_version}
Provides:       tex(MnSymbolA5.tfm) = %{tl_version}, tex(MnSymbolA6.tfm) = %{tl_version}
Provides:       tex(MnSymbolA7.tfm) = %{tl_version}, tex(MnSymbolA8.tfm) = %{tl_version}
Provides:       tex(MnSymbolA9.tfm) = %{tl_version}, tex(MnSymbolB-Bold10.tfm) = %{tl_version}
Provides:       tex(MnSymbolB-Bold12.tfm) = %{tl_version}
Provides:       tex(MnSymbolB-Bold5.tfm) = %{tl_version}
Provides:       tex(MnSymbolB-Bold6.tfm) = %{tl_version}
Provides:       tex(MnSymbolB-Bold7.tfm) = %{tl_version}
Provides:       tex(MnSymbolB-Bold8.tfm) = %{tl_version}
Provides:       tex(MnSymbolB-Bold9.tfm) = %{tl_version}
Provides:       tex(MnSymbolB10.tfm) = %{tl_version}, tex(MnSymbolB12.tfm) = %{tl_version}
Provides:       tex(MnSymbolB5.tfm) = %{tl_version}, tex(MnSymbolB6.tfm) = %{tl_version}
Provides:       tex(MnSymbolB7.tfm) = %{tl_version}, tex(MnSymbolB8.tfm) = %{tl_version}
Provides:       tex(MnSymbolB9.tfm) = %{tl_version}, tex(MnSymbolC-Bold10.tfm) = %{tl_version}
Provides:       tex(MnSymbolC-Bold12.tfm) = %{tl_version}
Provides:       tex(MnSymbolC-Bold5.tfm) = %{tl_version}
Provides:       tex(MnSymbolC-Bold6.tfm) = %{tl_version}
Provides:       tex(MnSymbolC-Bold7.tfm) = %{tl_version}
Provides:       tex(MnSymbolC-Bold8.tfm) = %{tl_version}
Provides:       tex(MnSymbolC-Bold9.tfm) = %{tl_version}
Provides:       tex(MnSymbolC10.tfm) = %{tl_version}, tex(MnSymbolC12.tfm) = %{tl_version}
Provides:       tex(MnSymbolC5.tfm) = %{tl_version}, tex(MnSymbolC6.tfm) = %{tl_version}
Provides:       tex(MnSymbolC7.tfm) = %{tl_version}, tex(MnSymbolC8.tfm) = %{tl_version}
Provides:       tex(MnSymbolC9.tfm) = %{tl_version}, tex(MnSymbolD-Bold10.tfm) = %{tl_version}
Provides:       tex(MnSymbolD-Bold12.tfm) = %{tl_version}
Provides:       tex(MnSymbolD-Bold5.tfm) = %{tl_version}
Provides:       tex(MnSymbolD-Bold6.tfm) = %{tl_version}
Provides:       tex(MnSymbolD-Bold7.tfm) = %{tl_version}
Provides:       tex(MnSymbolD-Bold8.tfm) = %{tl_version}
Provides:       tex(MnSymbolD-Bold9.tfm) = %{tl_version}
Provides:       tex(MnSymbolD10.tfm) = %{tl_version}, tex(MnSymbolD12.tfm) = %{tl_version}
Provides:       tex(MnSymbolD5.tfm) = %{tl_version}, tex(MnSymbolD6.tfm) = %{tl_version}
Provides:       tex(MnSymbolD7.tfm) = %{tl_version}, tex(MnSymbolD8.tfm) = %{tl_version}
Provides:       tex(MnSymbolD9.tfm) = %{tl_version}, tex(MnSymbolE-Bold10.tfm) = %{tl_version}
Provides:       tex(MnSymbolE-Bold12.tfm) = %{tl_version}
Provides:       tex(MnSymbolE-Bold5.tfm) = %{tl_version}
Provides:       tex(MnSymbolE-Bold6.tfm) = %{tl_version}
Provides:       tex(MnSymbolE-Bold7.tfm) = %{tl_version}
Provides:       tex(MnSymbolE-Bold8.tfm) = %{tl_version}
Provides:       tex(MnSymbolE-Bold9.tfm) = %{tl_version}
Provides:       tex(MnSymbolE10.tfm) = %{tl_version}, tex(MnSymbolE12.tfm) = %{tl_version}
Provides:       tex(MnSymbolE5.tfm) = %{tl_version}, tex(MnSymbolE6.tfm) = %{tl_version}
Provides:       tex(MnSymbolE7.tfm) = %{tl_version}, tex(MnSymbolE8.tfm) = %{tl_version}
Provides:       tex(MnSymbolE9.tfm) = %{tl_version}, tex(MnSymbolF-Bold10.tfm) = %{tl_version}
Provides:       tex(MnSymbolF-Bold12.tfm) = %{tl_version}
Provides:       tex(MnSymbolF-Bold5.tfm) = %{tl_version}
Provides:       tex(MnSymbolF-Bold6.tfm) = %{tl_version}
Provides:       tex(MnSymbolF-Bold7.tfm) = %{tl_version}
Provides:       tex(MnSymbolF-Bold8.tfm) = %{tl_version}
Provides:       tex(MnSymbolF-Bold9.tfm) = %{tl_version}
Provides:       tex(MnSymbolF10.tfm) = %{tl_version}, tex(MnSymbolF12.tfm) = %{tl_version}
Provides:       tex(MnSymbolF5.tfm) = %{tl_version}, tex(MnSymbolF6.tfm) = %{tl_version}
Provides:       tex(MnSymbolF7.tfm) = %{tl_version}, tex(MnSymbolF8.tfm) = %{tl_version}
Provides:       tex(MnSymbolF9.tfm) = %{tl_version}, tex(MnSymbolS-Bold10.tfm) = %{tl_version}
Provides:       tex(MnSymbolS-Bold12.tfm) = %{tl_version}
Provides:       tex(MnSymbolS-Bold5.tfm) = %{tl_version}
Provides:       tex(MnSymbolS-Bold6.tfm) = %{tl_version}
Provides:       tex(MnSymbolS-Bold7.tfm) = %{tl_version}
Provides:       tex(MnSymbolS-Bold8.tfm) = %{tl_version}
Provides:       tex(MnSymbolS-Bold9.tfm) = %{tl_version}
Provides:       tex(MnSymbolS10.tfm) = %{tl_version}, tex(MnSymbolS12.tfm) = %{tl_version}
Provides:       tex(MnSymbolS5.tfm) = %{tl_version}, tex(MnSymbolS6.tfm) = %{tl_version}
Provides:       tex(MnSymbolS7.tfm) = %{tl_version}, tex(MnSymbolS8.tfm) = %{tl_version}
Provides:       tex(MnSymbolS9.tfm) = %{tl_version}, tex(MnSymbol-Bold10.pfb) = %{tl_version}
Provides:       tex(MnSymbol-Bold12.pfb) = %{tl_version}
Provides:       tex(MnSymbol-Bold5.pfb) = %{tl_version}, tex(MnSymbol-Bold6.pfb) = %{tl_version}
Provides:       tex(MnSymbol-Bold7.pfb) = %{tl_version}, tex(MnSymbol-Bold8.pfb) = %{tl_version}
Provides:       tex(MnSymbol-Bold9.pfb) = %{tl_version}, tex(MnSymbol10.pfb) = %{tl_version}
Provides:       tex(MnSymbol12.pfb) = %{tl_version}, tex(MnSymbol5.pfb) = %{tl_version}
Provides:       tex(MnSymbol6.pfb) = %{tl_version}, tex(MnSymbol7.pfb) = %{tl_version}
Provides:       tex(MnSymbol8.pfb) = %{tl_version}, tex(MnSymbol9.pfb) = %{tl_version}
Provides:       tex(MnSymbol.sty) = %{tl_version}

%description -n texlive-mnsymbol
MnSymbol is a symbol font family, designed to be used in
conjunction with Adobe Minion Pro (via the MinionPro package).
Almost all of LaTeX and AMS mathematical symbols are provided;
remaining coverage is available from the MinionPro font with
the MinionPro package. The fonts are available both as Metafont
source and as Adobe Type 1 format, and a comprehensive support
package is provided. While the fonts were designed to fit with
Minon Pro, the design should fit well with other renaissance or
baroque faces: indeed, it will probably work with most fonts
that are neither too wide nor too thin, for example Palatino or
Times; it is known to look good with Sabon. There is no package
designed to configure its use with any font other than Minion
Pro, but (for example) simply loading mnsymbol after mathpazo
will probably do what is needed.

%package -n texlive-mnsymbol-doc
Summary:        Documentation for mnsymbol
Version:        svn18651.1.4

Provides:       tex-mnsymbol-doc
AutoReqProv:    No

%description -n texlive-mnsymbol-doc
Documentation for mnsymbol

%package -n texlive-marvosym
Provides:       tex-marvosym = %{tl_version}
License:        OFL
Summary:        Martin Vogel's Symbols (marvosym) font
Version:        svn29349.2.2a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(marvosym.map) = %{tl_version}, tex(umvs.tfm) = %{tl_version}
Provides:       tex(marvosym.ttf) = %{tl_version}, tex(marvosym.pfb) = %{tl_version}
Provides:       tex(marvosym.sty) = %{tl_version}, tex(umvs.fd) = %{tl_version}

%description -n texlive-marvosym
Martin Vogel's Symbol font (marvosym) contains the Euro
currency symbol as defined by the European commission, along
with symbols for structural engineering; symbols for steel
cross-sections; astronomy signs (sun, moon, planets); the 12
signs of the zodiac; scissor symbols; CE sign and others. The
package contains both the original TrueType font and the
derived Type 1 font, together with support files for TeX
(LaTeX).

%package -n texlive-marvosym-doc
Summary:        Documentation for marvosym
Version:        svn29349.2.2a

Provides:       tex-marvosym-doc
AutoReqProv:    No

%description -n texlive-marvosym-doc
Documentation for marvosym

%package -n texlive-mathpazo
Provides:       tex-mathpazo = %{tl_version}
License:        GPL+
Summary:        Fonts to typeset mathematics to match Palatino
Version:        svn15878.1.003

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fplmb.tfm) = %{tl_version}, tex(fplmbb.tfm) = %{tl_version}
Provides:       tex(fplmbi.tfm) = %{tl_version}, tex(fplmr.tfm) = %{tl_version}
Provides:       tex(fplmri.tfm) = %{tl_version}, tex(zplmb7m.tfm) = %{tl_version}
Provides:       tex(zplmb7t.tfm) = %{tl_version}, tex(zplmb7y.tfm) = %{tl_version}
Provides:       tex(zplmr7m.tfm) = %{tl_version}, tex(zplmr7t.tfm) = %{tl_version}
Provides:       tex(zplmr7v.tfm) = %{tl_version}, tex(zplmr7y.tfm) = %{tl_version}
Provides:       tex(fplmb.pfb) = %{tl_version}, tex(fplmbb.pfb) = %{tl_version}
Provides:       tex(fplmbi.pfb) = %{tl_version}, tex(fplmr.pfb) = %{tl_version}
Provides:       tex(fplmri.pfb) = %{tl_version}, tex(zplmb7m.vf) = %{tl_version}
Provides:       tex(zplmb7t.vf) = %{tl_version}, tex(zplmb7y.vf) = %{tl_version}
Provides:       tex(zplmr7m.vf) = %{tl_version}, tex(zplmr7t.vf) = %{tl_version}
Provides:       tex(zplmr7v.vf) = %{tl_version}, tex(zplmr7y.vf) = %{tl_version}

%description -n texlive-mathpazo
The Pazo Math fonts are a family of PostScript fonts suitable
for typesetting mathematics in combination with the Palatino
family of text fonts. The Pazo Math family is made up of five
fonts provided in Adobe Type 1 format (PazoMath, PazoMath-
Italic, PazoMath-Bold, PazoMath-BoldItalic, and
PazoMathBlackboardBold). These contain, in designs that match
Palatino, glyphs that are usually not available in Palatino and
for which Computer Modern looks odd when combined with
Palatino. These glyphs include the uppercase Greek alphabet in
upright and slanted shapes in regular and bold weights, the
lowercase Greek alphabet in slanted shape in regular and bold
weights, several mathematical glyphs (partialdiff, summation,
product, coproduct, emptyset, infinity, and proportional) in
regular and bold weights, other glyphs (Euro and dotlessj) in
upright and slanted shapes in regular and bold weights, and the
uppercase letters commonly used to represent various number
sets (C, I, N, Q, R, and Z) in blackboard bold. The set also
includes a set of 'true' small-caps fonts, also suitable for
use with Palatino (or one of its clones). LaTeX macro support
(using package mathpazo.sty) is provided in psnfss (a required
part of any LaTeX distribution).

%package -n texlive-mathpazo-doc
Summary:        Documentation for mathpazo
Version:        svn15878.1.003

Provides:       tex-mathpazo-doc
AutoReqProv:    No

%description -n texlive-mathpazo-doc
Documentation for mathpazo

%package -n texlive-mathdots
Provides:       tex-mathdots = %{tl_version}
License:        LPPL
Summary:        Commands to produce dots in math that respect font size
Version:        svn34301.0.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mathdots.sty) = %{tl_version}, tex(mathdots.tex) = %{tl_version}

%description -n texlive-mathdots
Redefines \ddots and \vdots, and defines \iddots. The dots
produced by \iddots slant in the opposite direction to \ddots.
All the commands are designed to change size appropriately in
scripts, as well as in response to LaTeX size changing
commands. The commands may also be used in plain TeX.

%package -n texlive-mathdots-doc
Summary:        Documentation for mathdots
Version:        svn34301.0.9

Provides:       tex-mathdots-doc
AutoReqProv:    No

%description -n texlive-mathdots-doc
Documentation for mathdots

%package -n texlive-metatex
Provides:       tex-metatex = %{tl_version}
License:        GPL+
Summary:        Incorporate Metafont pictures in TeX source
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(metatex.tex) = %{tl_version}

%description -n texlive-metatex
METATeX is a set of plain TeX and Metafont macros that you can
use to define both the text and the figures in a single source
file. Because METATeX sets up two way communication, from TeX
to Metafont and back from Metafont to TeX, drawing dimensions
can be controlled by TeX and labels can be located by Metafont.
Only standard features of TeX and Metafont are used, but two
runs of TeX and one of Metafont are needed.

%package -n texlive-metatex-doc
Summary:        Documentation for metatex
Version:        svn15878.1.1

Provides:       tex-metatex-doc
AutoReqProv:    No

%description -n texlive-metatex-doc
Documentation for metatex

%package -n texlive-midnight
Provides:       tex-midnight = %{tl_version}
License:        midnight
Summary:        A set of useful macro tools
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(border.tex) = %{tl_version}, tex(dolines.tex) = %{tl_version}
Provides:       tex(gloss.tex) = %{tl_version}, tex(labels.tex) = %{tl_version}
Provides:       tex(loop.tex) = %{tl_version}, tex(quire.tex) = %{tl_version}
Provides:       tex(styledef.tex) = %{tl_version}

%description -n texlive-midnight
Included are: quire: making booklets, etc.; gloss: vertically
align words in consecutive sentences; loop: a looping
construct; dolines: 'meta'-macros to separate arguments by
newlines; labels: address labels and bulk mail letters;
styledef: selectively input part of a file; and border: borders
around boxes.

%package -n texlive-midnight-doc
Summary:        Documentation for midnight
Version:        svn15878.0

Provides:       tex-midnight-doc
AutoReqProv:    No

%description -n texlive-midnight-doc
Documentation for midnight

%package -n texlive-metrix
Provides:       tex-metrix = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset metric marks for Latin text
Version:        svn40099

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty), tex(xpatch.sty), tex(tikz.sty)
Provides:       tex(metrix.sty) = %{tl_version}

%description -n texlive-metrix
The package may be used to type the prosodics/metrics of
(latin) verse; it provides macros to typeset the symbols
standing alone, and in combination with symbols, giving
automatic alignment. The package requires tikz (including the
calc library, and the xparse package (thus also requiring the
experimental LaTeX 3 environment).

%package -n texlive-metrix-doc
Summary:        Documentation for metrix
Version:        svn40099

Provides:       tex-metrix-doc
AutoReqProv:    No

%description -n texlive-metrix-doc
Documentation for metrix

%package -n texlive-macros2e-doc
Summary:        Documentation for macros2e
Version:        svn23236.v0.4

Provides:       tex-macros2e-doc
AutoReqProv:    No

%description -n texlive-macros2e-doc
Documentation for macros2e

%package -n texlive-math-e-doc
Summary:        Documentation for math-e
Version:        svn20062.0

Provides:       tex-math-e-doc
AutoReqProv:    No

%description -n texlive-math-e-doc
Documentation for math-e

%package -n texlive-maths-symbols-doc
Summary:        Documentation for maths-symbols
Version:        svn37763.3.4

Provides:       tex-maths-symbols-doc
AutoReqProv:    No

%description -n texlive-maths-symbols-doc
Documentation for maths-symbols

%package -n texlive-memdesign-doc
Summary:        Documentation for memdesign
Version:        svn34157.0

Provides:       tex-memdesign-doc
AutoReqProv:    No

%description -n texlive-memdesign-doc
Documentation for memdesign

%package -n texlive-metafont-beginners-doc
Summary:        Documentation for metafont-beginners
Version:        svn29803.0

Provides:       tex-metafont-beginners-doc
AutoReqProv:    No

%description -n texlive-metafont-beginners-doc
Documentation for metafont-beginners

%package -n texlive-metapost-examples-doc
Summary:        Documentation for metapost-examples
Version:        svn15878.0

Provides:       tex-metapost-examples-doc
AutoReqProv:    No

%description -n texlive-metapost-examples-doc
Documentation for metapost-examples

%package -n texlive-mafr
Provides:       tex-mafr = %{tl_version}
License:        GPL+
Summary:        Mathematics in accord with French usage
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(a4wide.sty), tex(fontenc.sty), tex(babel.sty)
Provides:       tex(cours.cls) = %{tl_version}, tex(fiche.cls) = %{tl_version}
Provides:       tex(mafr.sty) = %{tl_version}

%description -n texlive-mafr
The package provides settings and macros for typesetting
mathematics with LaTeX in compliance with French usage. It
comes with two document classes, 'fiche' and 'cours', useful to
create short high school documents such as tests or lessons.
The documentation is in French.

%package -n texlive-mafr-doc
Summary:        Documentation for mafr
Version:        svn15878.1.0

Provides:       tex-mafr-doc
AutoReqProv:    No

%description -n texlive-mafr-doc
Documentation for mafr

%package -n texlive-microtype-de-doc
Summary:        Documentation for microtype-de
Version:        svn24549.2.4

Provides:       tex-microtype-de-doc
AutoReqProv:    No

%description -n texlive-microtype-de-doc
Documentation for microtype-de

%package -n texlive-memoir
Provides:       tex-memoir = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset fiction, non-fiction and mathematical books
Version:        svn47305
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifpdf.sty), tex(ifetex.sty), tex(ifxetex.sty), tex(ifluatex.sty)
Requires:       tex(etex.sty)
Provides:       tex(mem10.clo) = %{tl_version}, tex(mem11.clo) = %{tl_version}
Provides:       tex(mem12.clo) = %{tl_version}, tex(mem14.clo) = %{tl_version}
Provides:       tex(mem17.clo) = %{tl_version}, tex(mem20.clo) = %{tl_version}
Provides:       tex(mem25.clo) = %{tl_version}, tex(mem30.clo) = %{tl_version}
Provides:       tex(mem36.clo) = %{tl_version}, tex(mem48.clo) = %{tl_version}
Provides:       tex(mem60.clo) = %{tl_version}, tex(mem9.clo) = %{tl_version}
Provides:       tex(memhfixc.sty) = %{tl_version}, tex(memoir.cls) = %{tl_version}
Provides:       tex(mempatch.sty) = %{tl_version}

%description -n texlive-memoir
The memoir class is for typesetting poetry, fiction, non-
fiction, and mathematical works. Permissible document 'base'
font sizes range from 9 to 60pt. There is a range of page-
styles and well over a dozen chapter-styles to choose from, as
well as methods for specifying your own layouts and designs.
The class also provides the functionality of over thirty of the
more popular packages, thus simplifying document sources. The
class automatically loads an associated patch file mempatch;
the patch file may be updated from time to time, between
releases of the class itself. (The patch file stays around even
when there are no extant patches.) Users who wish to use the
hyperref package, in a document written with the memoir class,
should also use the memhfixc package (part of this bundle).
Note, however, that any current version of hyperref actually
loads the package automatically if it detects that it is
running under memoir.

%package -n texlive-memoir-doc
Summary:        Documentation for memoir
Version:        svn47305
Provides:       tex-memoir-doc
AutoReqProv:    No

%description -n texlive-memoir-doc
Documentation for memoir

%package -n texlive-mathtools
Provides:       tex-mathtools = %{tl_version}
License:        LPPL 1.3
Summary:        Mathematical tools to use with amsmath
Version:        svn46250
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(mathtools.sty), tex(keyval.sty), tex(calc.sty), tex(amsmath.sty)
Requires:       tex(graphicx.sty)
Provides:       tex(empheq.sty) = %{tl_version}, tex(mathtools.sty) = %{tl_version}
Provides:       tex(mhsetup.sty) = %{tl_version}

%description -n texlive-mathtools
Mathtools provides a series of packages designed to enhance the
appearance of documents containing a lot of mathematics. The
main backbone is amsmath, so those unfamiliar with this
required part of the LaTeX system will probably not find the
packages very useful. Mathtools provides many useful tools for
mathematical typesetting. It is based on amsmath and fixes
various deficiencies of amsmath and standard LaTeX. It
provides: Extensible symbols, such as brackets, arrows,
harpoons, etc.; Various symbols such as \coloneqq (:=); Easy
creation of new tag forms; Showing equation numbers only for
referenced equations; Extensible arrows, harpoons and
hookarrows; Starred versions of the amsmath matrix environments
for specifying the column alignment; More building blocks:
multlined, cases-like environments, new gathered environments;
Maths versions of \makebox, \llap, \rlap etc.; Cramped math
styles; and more... Mathtools requires mhsetup.

%package -n texlive-mathtools-doc
Summary:        Documentation for mathtools
Version:        svn46250
Provides:       tex-mathtools-doc
AutoReqProv:    No

%description -n texlive-mathtools-doc
Documentation for mathtools

%package -n texlive-mdwtools
Provides:       tex-mdwtools = %{tl_version}
License:        GPL+
Summary:        Miscellaneous tools by Mark Wooding
Version:        svn15878.1.05.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(at.sty) = %{tl_version}, tex(cmtt.sty) = %{tl_version}
Provides:       tex(doafter.sty) = %{tl_version}, tex(footnote.sty) = %{tl_version}
Provides:       tex(mTTcmtt.fd) = %{tl_version}, tex(mTTenc.def) = %{tl_version}
Provides:       tex(mathenv.sty) = %{tl_version}, tex(mdwlist.sty) = %{tl_version}
Provides:       tex(mdwmath.sty) = %{tl_version}, tex(mdwtab.sty) = %{tl_version}
Provides:       tex(sverb.sty) = %{tl_version}, tex(syntax.sty) = %{tl_version}

%description -n texlive-mdwtools
This collection of tools includes: support for short commands
starting with @, macros to sanitise the OT1 encoding of the
cmtt fonts; a 'do after' command; improved footnote support;
mathenv for various alignment in maths; list handling; mdwmath
which adds some minor changes to LaTeX maths; a rewrite of
LaTeX's tabular and array environments; verbatim handling; and
syntax diagrams.

%package -n texlive-mdwtools-doc
Summary:        Documentation for mdwtools
Version:        svn15878.1.05.4

Provides:       tex-mdwtools-doc
AutoReqProv:    No

%description -n texlive-mdwtools-doc
Documentation for mdwtools

%package -n texlive-metalogo
Provides:       tex-metalogo = %{tl_version}
License:        LPPL
Summary:        Extended TeX logo macros
Version:        svn18611.0.12

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(ifxetex.sty), tex(fontspec.sty)
Provides:       tex(metalogo.sty) = %{tl_version}

%description -n texlive-metalogo
This package exposes spacing parameters for various TeX logos
to the end user, to optimise the logos for different fonts.
Written especially for XeLaTeX users.

%package -n texlive-metalogo-doc
Summary:        Documentation for metalogo
Version:        svn18611.0.12

Provides:       tex-metalogo-doc
AutoReqProv:    No

%description -n texlive-metalogo-doc
Documentation for metalogo

%package -n texlive-microtype
Provides:       tex-microtype = %{tl_version}
License:        LPPL
Summary:        Subliminal refinements towards typographical perfection
Version:        svn46323
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(letterspace.sty) = %{tl_version}, tex(microtype-luatex.def) = %{tl_version}
Provides:       tex(microtype-pdftex.def) = %{tl_version}
Provides:       tex(microtype-xetex.def) = %{tl_version}
Provides:       tex(microtype.cfg) = %{tl_version}, tex(microtype.sty) = %{tl_version}
Provides:       tex(mt-CharisSIL.cfg) = %{tl_version}, tex(mt-LatinModernRoman.cfg) = %{tl_version}
Provides:       tex(mt-PalatinoLinotype.cfg) = %{tl_version}
Provides:       tex(mt-bch.cfg) = %{tl_version}, tex(mt-blg.cfg) = %{tl_version}
Provides:       tex(mt-cmr.cfg) = %{tl_version}, tex(mt-euf.cfg) = %{tl_version}
Provides:       tex(mt-eur.cfg) = %{tl_version}, tex(mt-euroitc.cfg) = %{tl_version}
Provides:       tex(mt-eus.cfg) = %{tl_version}, tex(mt-msa.cfg) = %{tl_version}
Provides:       tex(mt-msb.cfg) = %{tl_version}, tex(mt-mvs.cfg) = %{tl_version}
Provides:       tex(mt-pad.cfg) = %{tl_version}, tex(mt-pmn.cfg) = %{tl_version}
Provides:       tex(mt-ppl.cfg) = %{tl_version}, tex(mt-ptm.cfg) = %{tl_version}
Provides:       tex(mt-ugm.cfg) = %{tl_version}, tex(mt-zpeu.cfg) = %{tl_version}

%description -n texlive-microtype
The package provides a LaTeX interface to the micro-typographic
extensions that were introduced by pdfTeX and have since also
propagated to XeTeX and LuaTeX: most prominently, character
protrusion and font expansion, furthermore the adjustment of
interword spacing and additional kerning, as well as
hyphenatable letterspacing (tracking) and the possibility to
disable all or selected ligatures. These features may be
applied to customisable sets of fonts, and all micro-
typographic aspects of the fonts can be configured in a
straight-forward and flexible way. Settings for various fonts
are provided. Note that character protrusion requires pdfTeX,
LuaTeX, or XeTeX. Font expansion works with pdfTeX or LuaTeX.
The package will by default enable protrusion and expansion if
they can safely be assumed to work. Disabling ligatures
requires pdfTeX or LuaTeX, while the adjustment of interword
spacing and of kerning only works with pdfTeX. Letterspacing is
available with pdfTeX or LuaTeX. The alternative package
`letterspace', which also works with plain TeX, provides the
user commands for letterspacing only, omitting support for all
other extensions.

%package -n texlive-microtype-doc
Summary:        Documentation for microtype
Version:        svn46323
Provides:       tex-microtype-doc
AutoReqProv:    No

%description -n texlive-microtype-doc
Documentation for microtype

%package -n texlive-makeshape
Provides:       tex-makeshape = %{tl_version}
License:        LPPL 1.3
Summary:        Declare new PGF shapes
Version:        svn28973.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty)
Provides:       tex(makeshape.sty) = %{tl_version}

%description -n texlive-makeshape
The package simplifies production of custom shapes with correct
anchor borders, in PGF/TikZ; the only requirement is a PGF path
describing the anchor border. The package also provides macros
that help with the management of shape parameters, and the
definition of anchor points.

%package -n texlive-makeshape-doc
Summary:        Documentation for makeshape
Version:        svn28973.2.1

Provides:       tex-makeshape-doc
AutoReqProv:    No

%description -n texlive-makeshape-doc
Documentation for makeshape

%package -n texlive-miniplot
Provides:       tex-miniplot = %{tl_version}
License:        LPPL
Summary:        A package for easy figure arrangement
Version:        svn17483.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty), tex(graphicx.sty), tex(epsfig.sty)
Provides:       tex(miniplot.sty) = %{tl_version}

%description -n texlive-miniplot
MiniPlot is a package to help the LaTeX user typeset EPS
figures using an easy-to-use interface. Figures can be arranged
as one-figure-only or as a collection of figures in columns and
rows which can itself contain sub-figures in columns and rows.
Wrapped figures are also supported. This package provides
commands to display a framebox instead of the figure as the
graphics package does already but additionally it writes useful
information such as the label and scaling factor into these
boxes.

%package -n texlive-miniplot-doc
Summary:        Documentation for miniplot
Version:        svn17483.0

Provides:       tex-miniplot-doc
AutoReqProv:    No

%description -n texlive-miniplot-doc
Documentation for miniplot

%package -n texlive-macroswap
Provides:       tex-macroswap = %{tl_version}
License:        LPPL 1.2
Summary:        Swap the definitions of two LaTeX macros
Version:        svn31498.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(macroswap.sty) = %{tl_version}

%description -n texlive-macroswap
The package provides simple utility methods to swap the meaning
(token expansion) of two macros by name.

%package -n texlive-macroswap-doc
Summary:        Documentation for macroswap
Version:        svn31498.1.1

Provides:       tex-macroswap-doc
AutoReqProv:    No

%description -n texlive-macroswap-doc
Documentation for macroswap

%package -n texlive-magaz
Provides:       tex-magaz = %{tl_version}
License:        Copyright only
Summary:        Magazine layout
Version:        svn24694.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(magaz.sty) = %{tl_version}

%description -n texlive-magaz
The current version does special formatting for the first line
of text in a paragraph. The package is part of a larger body of
tools which remain in preparation.

%package -n texlive-magaz-doc
Summary:        Documentation for magaz
Version:        svn24694.0.4

Provides:       tex-magaz-doc
AutoReqProv:    No

%description -n texlive-magaz-doc
Documentation for magaz

%package -n texlive-mailing
Provides:       tex-mailing = %{tl_version}
License:        LPPL
Summary:        Macros for mail merging
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mailing.sty) = %{tl_version}

%description -n texlive-mailing
This package is for use when sending a large number of letters,
all with the same body text. The package's \addressfile command
is used to specify who the letter is to be sent to; the body of
the \mailingtext command specifies the text of the letters,
possibly using macros defined in the \addressfile.

%package -n texlive-mailing-doc
Summary:        Documentation for mailing
Version:        svn15878.0

Provides:       tex-mailing-doc
AutoReqProv:    No

%description -n texlive-mailing-doc
Documentation for mailing

%package -n texlive-mailmerge
Provides:       tex-mailmerge = %{tl_version}
License:        LPPL 1.2
Summary:        Repeating text field substitution
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(mailmerge.sty) = %{tl_version}

%description -n texlive-mailmerge
The package mailmerge provides an interface to produce text
from a template, where fields are replaced by actual data, as
in a database. The package may be used to produce several
letters from a template, certificates or other such documents.
It allows access to the entry number, number of entries and so
on.

%package -n texlive-mailmerge-doc
Summary:        Documentation for mailmerge
Version:        svn15878.1.0

Provides:       tex-mailmerge-doc
AutoReqProv:    No

%description -n texlive-mailmerge-doc
Documentation for mailmerge

%package -n texlive-makebarcode
Provides:       tex-makebarcode = %{tl_version}
License:        LPPL
Summary:        Print various kinds 2/5 and Code 39 bar codes
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty)
Provides:       tex(makebarcode.sty) = %{tl_version}

%description -n texlive-makebarcode
The package contains macros for printing various 2/5 bar codes
and Code 39 bar codes. The macros do not use fonts but create
the bar codes directly using vertical rules. It is therefore
possible to vary width to height ratio, ratio of thin and thick
bars. The package is therefore convenient for printing ITF bar
codes as well as bar codes for identification labels for HP
storage media.

%package -n texlive-makebarcode-doc
Summary:        Documentation for makebarcode
Version:        svn15878.1.0

Provides:       tex-makebarcode-doc
AutoReqProv:    No

%description -n texlive-makebarcode-doc
Documentation for makebarcode

%package -n texlive-makebox
Provides:       tex-makebox = %{tl_version}
License:        LPPL
Summary:        Defines a \makebox* command
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(makebox.sty) = %{tl_version}

%description -n texlive-makebox
Define a \makebox* command that does the same as a \makebox
command, except that the width is given by a sample text
instead of an explicit length measure.

%package -n texlive-makebox-doc
Summary:        Documentation for makebox
Version:        svn15878.0.1

Provides:       tex-makebox-doc
AutoReqProv:    No

%description -n texlive-makebox-doc
Documentation for makebox

%package -n texlive-makecell
Provides:       tex-makecell = %{tl_version}
License:        LPPL
Summary:        Tabular column heads and multilined cells
Version:        svn15878.0.1e

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty)
Provides:       tex(makecell.sty) = %{tl_version}

%description -n texlive-makecell
This package supports common layouts for tabular column heads
in whole documents, based on one-column tabular environment. In
addition, it can create multi-lined tabular cells. The Package
also offers: a macro which changes the vertical space around
all the cells in a tabular environment (similar to the function
of the tabls package, but using the facilities of the array)
macros for multirow cells, which use the facilities of the
multirow package; macros to number rows in tables, or to skip
cells; diagonally divided cells; horizontal lines in tabular
environments with defined thickness.

%package -n texlive-makecell-doc
Summary:        Documentation for makecell
Version:        svn15878.0.1e

Provides:       tex-makecell-doc
AutoReqProv:    No

%description -n texlive-makecell-doc
Documentation for makecell

%package -n texlive-makecirc
Provides:       tex-makecirc = %{tl_version}
License:        LPPL
Summary:        A MetaPost library for drawing electrical circuit diagrams
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-makecirc
MakeCirc is a MetaPost library that contains diverse symbols
for use in circuit diagrams. MakeCirc offers a high quality
tool, with a simple syntax. MakeCirc is completely integrated
with LaTeX documents and with other MetaPost drawing/graphic.
Its output is a PostScript file. MakeCirc only requires (La)TeX
and MetaPost to work.

%package -n texlive-makecirc-doc
Summary:        Documentation for makecirc
Version:        svn15878.0

Provides:       tex-makecirc-doc
AutoReqProv:    No

%description -n texlive-makecirc-doc
Documentation for makecirc

%package -n texlive-makecmds
Provides:       tex-makecmds = %{tl_version}
License:        LPPL
Summary:        The new \makecommand command always (re)defines a command
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(makecmds.sty) = %{tl_version}

%description -n texlive-makecmds
The package provides a \makecommand command, which is like
\(re)newcommand except it always (re)defines a command. There
is also \makeenvironment and \provideenvironment for
environments.

%package -n texlive-makecmds-doc
Summary:        Documentation for makecmds
Version:        svn15878.0

Provides:       tex-makecmds-doc
AutoReqProv:    No

%description -n texlive-makecmds-doc
Documentation for makecmds

%package -n texlive-makeglos
Provides:       tex-makeglos = %{tl_version}
License:        GPL+
Summary:        Include a glossary into a document
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(makeglos.sty) = %{tl_version}

%description -n texlive-makeglos
The package provides the means to include a glossary into a
document. The glossary is prepared by an external program, such
as xindy or makeindex, in the same way that an index is made.

%package -n texlive-makeglos-doc
Summary:        Documentation for makeglos
Version:        svn15878.0

Provides:       tex-makeglos-doc
AutoReqProv:    No

%description -n texlive-makeglos-doc
Documentation for makeglos

%package -n texlive-mandi
Provides:       tex-mandi = %{tl_version}
License:        LPPL 1.3
Summary:        Macros for introductory physics and astronomy
Version:        svn47150
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(amsmath.sty), tex(amssymb.sty), tex(array.sty), tex(cancel.sty)
Requires:       tex(xcolor.sty), tex(environ.sty), tex(esint.sty), tex(esvect.sty)
Requires:       tex(etoolbox.sty), tex(filehook.sty), tex(extarrows.sty), tex(fontenc.sty)
Requires:       tex(graphicx.sty), tex(epstopdf.sty), tex(textcomp.sty), tex(letltxmacro.sty)
Requires:       tex(listings.sty), tex(mdframed.sty), tex(suffix.sty), tex(xargs.sty)
Requires:       tex(xparse.sty), tex(xspace.sty), tex(ifthen.sty), tex(calligra.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(mandi.sty) = %{tl_version}

%description -n texlive-mandi
The package contains commands for students and teachers of
introductory physics. Commands for physical quantities
intelligently handle SI units so the user need not do so. There
are other features that should make LaTeX easy for introductory
physics students.

%package -n texlive-mandi-doc
Summary:        Documentation for mandi
Version:        svn47150
Provides:       tex-mandi-doc
AutoReqProv:    No

%description -n texlive-mandi-doc
Documentation for mandi

%package -n texlive-manfnt
Provides:       tex-manfnt = %{tl_version}
License:        LPPL
Summary:        LaTeX support for the TeX book symbols
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(manfnt.sty) = %{tl_version}

%description -n texlive-manfnt
A LaTeX package for easy access to the symbols of the Knuth's
'manual' font, such as the Dangerous Bend and Manual-errata
Arrow.

%package -n texlive-manuscript
Provides:       tex-manuscript = %{tl_version}
License:        LPPL
Summary:        Emulate look of a document typed on a typewriter
Version:        svn36110.1.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(setspace.sty), tex(fontenc.sty), tex(ragged2e.sty), tex(soul.sty)
Requires:       tex(fullpage.sty)
Provides:       tex(manuscript.sty) = %{tl_version}

%description -n texlive-manuscript
This package is designed for those who have to submit
dissertations, etc., to institutions that still maintain the
typewriter is the summit of non-professional printing.

%package -n texlive-manuscript-doc
Summary:        Documentation for manuscript
Version:        svn36110.1.7

Provides:       tex-manuscript-doc
AutoReqProv:    No

%description -n texlive-manuscript-doc
Documentation for manuscript

%package -n texlive-marginfix
Provides:       tex-marginfix = %{tl_version}
License:        LPPL
Summary:        Patch \marginpar to avoid overfull margins
Version:        svn31598.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(marginfix.sty) = %{tl_version}

%description -n texlive-marginfix
Authors using LaTeX to typeset books with significant margin
material often run into the problem of long notes running off
the bottom of the page. A typical workaround is to insert
\vshift commands by hand, but this is a tedious process that is
invalidated when pagination changes. Another workaround is
memoir's \sidebar function, but this can be unsatisfying for
short textual notes, and standard marginpars cannot be mixed
with sidebars. This package implements a solution to make
marginpars "just work" by keeping a list of floating inserts
and arranging them intelligently in the output routine.

%package -n texlive-marginfix-doc
Summary:        Documentation for marginfix
Version:        svn31598.1.1

Provides:       tex-marginfix-doc
AutoReqProv:    No

%description -n texlive-marginfix-doc
Documentation for marginfix

%package -n texlive-marginnote
Provides:       tex-marginnote = %{tl_version}
License:        LPPL
Summary:        Notes in the margin, even where \marginpar fails
Version:        svn48383
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(marginnote.sty) = %{tl_version}

%description -n texlive-marginnote
This package provides the command \marginnote that may be used
instead of \marginpar at almost every place where \marginpar
cannot be used, e.g., inside floats, footnotes, or in frames
made with the framed package.

%package -n texlive-marginnote-doc
Summary:        Documentation for marginnote
Version:        svn48383
Provides:       tex-marginnote-doc
AutoReqProv:    No

%description -n texlive-marginnote-doc
Documentation for marginnote

%package -n texlive-mathalfa
Provides:       tex-mathalfa = %{tl_version}
License:        LPPL 1.3
Summary:        General package for loading maths alphabets in LaTeX
Version:        svn47575
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(mathalfa.sty) = %{tl_version}

%description -n texlive-mathalfa
The package provides means of loading maths alphabets (such as
are normally addressed via macros \mathcal, \mathbb, \mathfrak
and \mathscr), offering various features normally missing in
existing packages for this job.

%package -n texlive-mathalfa-doc
Summary:        Documentation for mathalfa
Version:        svn47575
Provides:       tex-mathalfa-doc
AutoReqProv:    No

%description -n texlive-mathalfa-doc
Documentation for mathalfa

%package -n texlive-mathastext
Provides:       tex-mathastext = %{tl_version}
License:        LPPL 1.3
Summary:        Use the text font in maths mode
Version:        svn42447
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(mathastext.sty) = %{tl_version}

%description -n texlive-mathastext
The package uses a text font (usually the document's text font)
for the letters of the Latin alphabet needed when typesetting
mathematics. (Optionally, other characters in the font may also
be used). This facility makes possible (for a document with
simple mathematics) a far wider choice of text font, with
little worry that no specially designed accompanying maths
fonts are available. The package also offers a simple mechanism
for using many different choices of (text hence, now, maths)
font in the same document. Of course, using one font for two
purposes helps produce smaller PDF files. The package, running
under LuaTeX, requires the TeX live 2013 distribution (or
later).

%package -n texlive-mathastext-doc
Summary:        Documentation for mathastext
Version:        svn42447
Provides:       tex-mathastext-doc
AutoReqProv:    No

%description -n texlive-mathastext-doc
Documentation for mathastext

%package -n texlive-mathexam
Provides:       tex-mathexam = %{tl_version}
License:        LPPL
Summary:        Package for typesetting exams
Version:        svn15878.1.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fancyhdr.sty), tex(lastpage.sty), tex(ifthen.sty)
Provides:       tex(mathexam.sty) = %{tl_version}

%description -n texlive-mathexam
The package can help you typeset exams (mostly in mathematics
and related disciplines where students are required to show
their calculations followed by one or more short answers). It
provides commands for inclusion of space for calculations, as
well as commands for automatic creation of "answer spaces". In
addition, the package will automatically create page headers
and footers, and will let you include instructions and space
for students to put their name.

%package -n texlive-mathexam-doc
Summary:        Documentation for mathexam
Version:        svn15878.1.00

Provides:       tex-mathexam-doc
AutoReqProv:    No

%description -n texlive-mathexam-doc
Documentation for mathexam

%package -n texlive-maybemath
Provides:       tex-maybemath = %{tl_version}
License:        LPPL
Summary:        Make math bold or italic according to context
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(bm.sty)
Provides:       tex(maybemath.sty) = %{tl_version}

%description -n texlive-maybemath
The \maybebm and \maybeit macros can be used in maths
expressions to make the arguments typeset as bold or italic
respectively if the surrounding context is appropriate. They
are useful for writing user macros for use in general contexts.
\maybebm is especially appropriate when section titles contain
math expressions, since the title will appear bold but the
header and table of contents usually replicate the title in
normal width. It uses the bm package to make things bold
\maybeit performs a similar role to \mathrm{} but the maths
expression will be italicised if the surrounding text is.
\maybeitsubscript is provided to shift subscripts to the left
if the expression is italicised.

%package -n texlive-maybemath-doc
Summary:        Documentation for maybemath
Version:        svn15878.0

Provides:       tex-maybemath-doc
AutoReqProv:    No

%description -n texlive-maybemath-doc
Documentation for maybemath

%package -n texlive-mbenotes
Provides:       tex-mbenotes = %{tl_version}
License:        LPPL 1.2
Summary:        Notes in tables or images
Version:        svn31813.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(xcolor.sty)
Provides:       tex(mbenotes.sty) = %{tl_version}

%description -n texlive-mbenotes
The package defines a command \tabnote, which stores notes for
later processing by the command \thetabnotes, and a
corresponding \imgnote for images. The package is derived from
mechanisms in the package endnotes.

%package -n texlive-mbenotes-doc
Summary:        Documentation for mbenotes
Version:        svn31813.2

Provides:       tex-mbenotes-doc
AutoReqProv:    No

%description -n texlive-mbenotes-doc
Documentation for mbenotes

%package -n texlive-mcaption
Provides:       tex-mcaption = %{tl_version}
License:        LPPL
Summary:        Put captions in the margin
Version:        svn15878.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(changepage.sty)
Provides:       tex(mcaption.sty) = %{tl_version}

%description -n texlive-mcaption
The mcaption package provides an mcaption environment which
puts figure or table captions in the margin. The package works
with the standard classes and with the KOMA-Script document
classes scrartcl, scrreprt and scrbook. The package requires
the changepage package.

%package -n texlive-mcaption-doc
Summary:        Documentation for mcaption
Version:        svn15878.3.0

Provides:       tex-mcaption-doc
AutoReqProv:    No

%description -n texlive-mcaption-doc
Documentation for mcaption

%package -n texlive-mceinleger
Provides:       tex-mceinleger = %{tl_version}
License:        GPL+
Summary:        Creating covers for music cassettes
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mceinleger.sty) = %{tl_version}

%description -n texlive-mceinleger
A package for creating MC-covers on your own. It allows the
creation of simple covers as well as covers with an additional
page for more information about the cassette (table of contents
e.g.). The rotating package is required.

%package -n texlive-mceinleger-doc
Summary:        Documentation for mceinleger
Version:        svn15878.0

Provides:       tex-mceinleger-doc
AutoReqProv:    No

%description -n texlive-mceinleger-doc
Documentation for mceinleger

%package -n texlive-mcite
Provides:       tex-mcite = %{tl_version}
License:        GPL+
Summary:        Multiple items in a single citation
Version:        svn18173.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mcite.sty) = %{tl_version}

%description -n texlive-mcite
The mcite package allows the user to collapse multiple
citations into one, as is customary in physics journals. The
package requires a customised BibTeX style for its work; the
documentation explains how to do that customisation.

%package -n texlive-mcite-doc
Summary:        Documentation for mcite
Version:        svn18173.1.6

Provides:       tex-mcite-doc
AutoReqProv:    No

%description -n texlive-mcite-doc
Documentation for mcite

%package -n texlive-mciteplus
Provides:       tex-mciteplus = %{tl_version}
License:        LPPL
Summary:        Enhanced multiple citations
Version:        svn31648.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mciteplus.sty) = %{tl_version}

%description -n texlive-mciteplus
The mciteplus LaTeX package is an enhanced reimplementation of
Thorsten Ohl's mcite package which provides support for the
grouping of multiple citations together as is often done in
physics journals. An extensive set of features provide for
other applications such as reference sublisting.

%package -n texlive-mciteplus-doc
Summary:        Documentation for mciteplus
Version:        svn31648.1.2

Provides:       tex-mciteplus-doc
AutoReqProv:    No

%description -n texlive-mciteplus-doc
Documentation for mciteplus

%package -n texlive-mdframed
Provides:       tex-mdframed = %{tl_version}
License:        LPPL
Summary:        Framed environments that can split at page boundaries
Version:        svn31075.1.9b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(l3keys2e.sty), tex(xparse.sty), tex(ifxetex.sty)
Requires:       tex(ifluatex.sty), tex(etoolbox.sty), tex(geometry.sty), tex(selinput.sty)
Requires:       tex(fontenc.sty), tex(beramono.sty), tex(microtype.sty), tex(fontspec.sty)
Requires:       tex(csquotes.sty), tex(xspace.sty), tex(multicol.sty), tex(scrpage2.sty)
Requires:       tex(enumitem.sty), tex(amsmath.sty), tex(listings.sty), tex(ntheorem.sty)
Requires:       tex(array.sty), tex(booktabs.sty), tex(xcolor.sty), tex(tikz.sty)
Requires:       tex(graphicx.sty), tex(hypdoc.sty), tex(showframe.sty), tex(lipsum.sty)
Requires:       tex(kantlipsum.sty), tex(kvoptions.sty), tex(zref-abspage.sty), tex(needspace.sty)
Requires:       tex(color.sty)
Provides:       tex(ltxmdf.cls) = %{tl_version}, tex(mdframed.sty) = %{tl_version}

%description -n texlive-mdframed
The package develops the facilities of framed in providing
breakable framed and coloured boxes. The user may instruct the
package to perform its operations using default LaTeX commands,
PStricks or TikZ.

%package -n texlive-mdframed-doc
Summary:        Documentation for mdframed
Version:        svn31075.1.9b

Provides:       tex-mdframed-doc
AutoReqProv:    No

%description -n texlive-mdframed-doc
Documentation for mdframed

%package -n texlive-media9
Provides:       tex-media9 = %{tl_version}
License:        LPPL 1.3
Summary:        Multimedia inclusion package with Adobe Reader-9/X compatibility
Version:        svn47957
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(l3regex.sty), tex(l3keys2e.sty), tex(xparse.sty)
Requires:       tex(ifpdf.sty), tex(atbegshi.sty), tex(atenddvi.sty), tex(tikz.sty)
Requires:       tex(pdftexcmds.sty)
Provides:       tex(media9.sty) = %{tl_version}, texlive-movie15 = svn26473.0.obsolete
Obsoletes:      texlive-movie15 <= svn26473.0

%description -n texlive-media9
The package provides an interface to embed interactive Flash
(SWF) and 3D objects (Adobe U3D & PRC), as well as video and
sound files or streams in the popular MP4, FLV and MP3 formats
into PDF documents with Acrobat-9/X compatibility. Playback of
multimedia files uses the built-in Flash Player of Adobe Reader
and does, therefore, not depend on external plug-ins. Flash
Player supports the efficient H.264 codec for video
compression. The package is based on the RichMedia Annotation,
an Adobe addition to the PDF specification. It replaces the now
obsolete movie15 package.

%package -n texlive-media9-doc
Summary:        Documentation for media9
Version:        svn47957
Provides:       tex-media9-doc
AutoReqProv:    No
Provides:       texlive-movie15-doc = svn26473.0.obsolete
Obsoletes:      texlive-movie15-doc <= svn26473.0

%description -n texlive-media9-doc
Documentation for media9

%package -n texlive-medstarbeamer
Provides:       tex-medstarbeamer = %{tl_version}
License:        LPPL 1.3
Summary:        Beamer document class for MedStar Health Research Institute
Version:        svn38828

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(anysize.sty), tex(hyperref.sty), tex(graphicx.sty), tex(pgf.sty)
Requires:       tex(xcolor.sty), tex(booktabs.sty), tex(soul.sty), tex(background.sty)
Requires:       tex(cancel.sty), tex(amsmath.sty), tex(enumerate.sty)
Provides:       tex(medstarbeamer.cls) = %{tl_version}

%description -n texlive-medstarbeamer
This is a beamer template for MedStar Health presentations. It
includes sample presentations using both .tex files and .rnw
files. The document class is obviously compatible with both.
The advantage of the .rnw file is that it can be used with
knitr such that you can weave your R code with your
presentation.

%package -n texlive-medstarbeamer-doc
Summary:        Documentation for medstarbeamer
Version:        svn38828

Provides:       tex-medstarbeamer-doc
AutoReqProv:    No

%description -n texlive-medstarbeamer-doc
Documentation for medstarbeamer

%package -n texlive-meetingmins
Provides:       tex-meetingmins = %{tl_version}
License:        LPPL 1.3
Summary:        Format written minutes of meetings
Version:        svn31878.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(fontenc.sty), tex(lmodern.sty), tex(fancyhdr.sty)
Requires:       tex(enumitem.sty), tex(mathabx.sty), tex(xstring.sty), tex(environ.sty)
Provides:       tex(meetingmins.cls) = %{tl_version}

%description -n texlive-meetingmins
The class allows formatting of meeting minutes using \section
commands (which provide hierarchical structure). An agenda can
also be produced for distribution prior to the meeting, with
user-selected portions suppressed from printing.

%package -n texlive-meetingmins-doc
Summary:        Documentation for meetingmins
Version:        svn31878.1.6

Provides:       tex-meetingmins-doc
AutoReqProv:    No

%description -n texlive-meetingmins-doc
Documentation for meetingmins

%package -n texlive-memexsupp
Provides:       tex-memexsupp = %{tl_version}
License:        LPPL
Summary:        Experimental memoir support
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(memexsupp.sty) = %{tl_version}

%description -n texlive-memexsupp
A package of code proposed as supporting material for memoir.
The package is intended as a test bed for such code, which may
in the fullness of time be adopted into the main memoir
release.

%package -n texlive-memexsupp-doc
Summary:        Documentation for memexsupp
Version:        svn15878.0.1

Provides:       tex-memexsupp-doc
AutoReqProv:    No

%description -n texlive-memexsupp-doc
Documentation for memexsupp

%package -n texlive-memory
Provides:       tex-memory = %{tl_version}
License:        LPPL 1.3
Summary:        Containers for data in LaTeX
Version:        svn30452.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(memory.sty) = %{tl_version}

%description -n texlive-memory
The package allows the user to declare single object or array
containers.

%package -n texlive-memory-doc
Summary:        Documentation for memory
Version:        svn30452.1.2

Provides:       tex-memory-doc
AutoReqProv:    No

%description -n texlive-memory-doc
Documentation for memory

%package -n texlive-menu
Provides:       tex-menu = %{tl_version}
License:        LPPL
Summary:        Typesetting menus
Version:        svn15878.0.994

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty), tex(bbding.sty), tex(fancybox.sty), tex(color.sty)
Provides:       tex(menu.sty) = %{tl_version}

%description -n texlive-menu
The package defines command \menu which assists typesetting of
a path through a program's menu.

%package -n texlive-menu-doc
Summary:        Documentation for menu
Version:        svn15878.0.994

Provides:       tex-menu-doc
AutoReqProv:    No

%description -n texlive-menu-doc
Documentation for menu

%package -n texlive-menukeys
Provides:       tex-menukeys = %{tl_version}
License:        LPPL 1.2
Summary:        Format menu sequences, paths and keystrokes from lists
Version:        svn41823
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xparse.sty), tex(xstring.sty), tex(etoolbox.sty), tex(tikz.sty)
Requires:       tex(xcolor.sty), tex(adjustbox.sty), tex(relsize.sty), tex(catoptions.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(menukeys.sty) = %{tl_version}

%description -n texlive-menukeys
The package allows easy input and formatting of menu sequences,
using menus set with commands such as \menu{Extras > Settings >
General}, paths using a command like
\path{macros/latex/contrib/menukeys} and short cuts such as
\keys{\ctrl + C}. The output is highly configurable by
providing different styles and colour themes.

%package -n texlive-menukeys-doc
Summary:        Documentation for menukeys
Version:        svn41823
Provides:       tex-menukeys-doc
AutoReqProv:    No

%description -n texlive-menukeys-doc
Documentation for menukeys

%package -n texlive-method
Provides:       tex-method = %{tl_version}
License:        LPPL
Summary:        Typeset method and variable declarations
Version:        svn17485.2.0b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(method.sty) = %{tl_version}

%description -n texlive-method
The package supports typesetting of programming language method
and variable declarations. It supports declarations in German,
French and English.

%package -n texlive-method-doc
Summary:        Documentation for method
Version:        svn17485.2.0b

Provides:       tex-method-doc
AutoReqProv:    No

%description -n texlive-method-doc
Documentation for method

%package -n texlive-metre
Provides:       tex-metre = %{tl_version}
License:        LPPL
Summary:        Support for the work of classicists
Version:        svn18489.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(relsize.sty)
Provides:       tex(metre.sty) = %{tl_version}

%description -n texlive-metre
The package provides classicists with some of the tools that
are needed for typesetting scholarly publications dealing with
Greek and Latin texts, with special emphasis on Greek verse. As
the package's name suggests, its core is a comprehensive set of
commands for generating metrical schemes and for placing
prosodical marks on text set in the Latin or the Greek
alphabet. The rest of the package provides a miscellany of
commands for symbols (most of them not directly related to
metre) that are often used in critical editions of classical
texts. The package does not require any special font: all
symbols are taken from the Computer Modern fonts (which are
included in all TeX distributions) and the package's commands
are based on TeX primitives.

%package -n texlive-metre-doc
Summary:        Documentation for metre
Version:        svn18489.1.0

Provides:       tex-metre-doc
AutoReqProv:    No

%description -n texlive-metre-doc
Documentation for metre

%package -n texlive-mfirstuc
Provides:       tex-mfirstuc = %{tl_version}
License:        LPPL 1.3
Summary:        Uppercase the first letter of a word
Version:        svn45803
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etoolbox.sty)
Provides:       tex(mfirstuc-english.sty) = %{tl_version}
Provides:       tex(mfirstuc.sty) = %{tl_version}

%description -n texlive-mfirstuc
The package provides commands \makefirstuc that uppercases the
first letter in its argument, and \xmakefirstuc which expands
the argument before uppercasing.

%package -n texlive-mfirstuc-doc
Summary:        Documentation for mfirstuc
Version:        svn45803
Provides:       tex-mfirstuc-doc
AutoReqProv:    No

%description -n texlive-mfirstuc-doc
Documentation for mfirstuc

%package -n texlive-mftinc
Provides:       tex-mftinc = %{tl_version}
License:        LPPL
Summary:        Pretty-print Metafont source
Version:        svn15878.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(rawfonts.sty), tex(keyval.sty), tex(chngpage.sty), tex(lineno.sty)
Provides:       tex(mftinc.sty) = %{tl_version}

%description -n texlive-mftinc
The mft program pretty-prints Metafont source code into a TeX
file. The mftinc package facilitates incorporating such files
into a LaTeX2e document. In addition, mftinc provides routines
for improved comment formatting and for typesetting font
tables.

%package -n texlive-mftinc-doc
Summary:        Documentation for mftinc
Version:        svn15878.1.0a

Provides:       tex-mftinc-doc
AutoReqProv:    No

%description -n texlive-mftinc-doc
Documentation for mftinc

%package -n texlive-midpage
Provides:       tex-midpage = %{tl_version}
License:        LPPL
Summary:        Environment for vertical centring
Version:        svn17484.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(midpage.sty) = %{tl_version}

%description -n texlive-midpage
The environment will centre text, if immediately preceded and
followed by \clearpage.

%package -n texlive-midpage-doc
Summary:        Documentation for midpage
Version:        svn17484.1.1a

Provides:       tex-midpage-doc
AutoReqProv:    No

%description -n texlive-midpage-doc
Documentation for midpage

%package -n texlive-minibox
Provides:       tex-minibox = %{tl_version}
License:        LPPL
Summary:        A simple type of box for LaTeX
Version:        svn30914.0.2a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty)
Provides:       tex(minibox.sty) = %{tl_version}

%description -n texlive-minibox
This small package provides a convenient input syntax for boxes
that don't break their text over lines automatically, but do
allow manual line breaks. The boxes shrink to the natural width
of the longest line they contain.

%package -n texlive-minibox-doc
Summary:        Documentation for minibox
Version:        svn30914.0.2a

Provides:       tex-minibox-doc
AutoReqProv:    No

%description -n texlive-minibox-doc
Documentation for minibox

%package -n texlive-minifp
Provides:       tex-minifp = %{tl_version}
License:        LPPL 1.3
Summary:        Fixed-point real computations to 8 decimals
Version:        svn32559.0.96

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mfpextra.tex) = %{tl_version}, tex(minifp.sty) = %{tl_version}

%description -n texlive-minifp
The package provides basic arithmetic operations to 8 decimal
places for plain TeX or LaTeX. Results are exact when they fit
within the digit limits. Along with the basic package is an
optional extension that adds computation of sin, cos, log,
sqrt, exp, powers and angles. These are also exact when
theoretically possible and are otherwise accurate to at least 7
decimal places. In addition, the package provides a stack-based
programing environment.

%package -n texlive-minifp-doc
Summary:        Documentation for minifp
Version:        svn32559.0.96

Provides:       tex-minifp-doc
AutoReqProv:    No

%description -n texlive-minifp-doc
Documentation for minifp

%package -n texlive-minipage-marginpar
Provides:       tex-minipage-marginpar = %{tl_version}
License:        LPPL
Summary:        Minipages with marginal notes
Version:        svn15878.v0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(minipage-marginpar.sty) = %{tl_version}
Provides:       tex(mpgmpar.sty) = %{tl_version}

%description -n texlive-minipage-marginpar
This package allows \marginpar-commands inside of minipages and
other boxes. (It takes another approach than marginnote by
Markus Kohm: it saves all \marginpar-commands and typesets them
outside (i.e., after) the box.) The package defines an
environment minipagewithmarginpars (to be used like minipage)--
and the internal commands may be used by other packages to
define similar environments or commands.

%package -n texlive-minipage-marginpar-doc
Summary:        Documentation for minipage-marginpar
Version:        svn15878.v0.2

Provides:       tex-minipage-marginpar-doc
AutoReqProv:    No

%description -n texlive-minipage-marginpar-doc
Documentation for minipage-marginpar

%package -n texlive-minitoc
Provides:       tex-minitoc = %{tl_version}
License:        LPPL 1.3
Summary:        Produce a table of contents for each chapter, part or section
Version:        svn48196
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(mtcpatchmem.sty), tex(flafter.sty), tex(placeins.sty), tex(notoccite.sty)
Provides:       tex(minitoc.sty) = %{tl_version}, tex(mtcmess.sty) = %{tl_version}
Provides:       tex(mtcoff.sty) = %{tl_version}, tex(mtcpatchmem.sty) = %{tl_version}

%description -n texlive-minitoc
The minitoc package allows you to add mini-tables-of-contents
(minitocs) at the beginning of every chapter, part or section.
There is also provision for mini-lists of figures and of
tables. At the part level, they are parttocs, partlofs and
partlots. If the type of document does not use chapters, the
basic provision is section level secttocs, sectlofs and
sectlots. The package has provision for language-specific
configuration of its own "fixed names", using .mld files
(analagous to babel .ldf files that do that job for LaTeX"s own
fixed names).

%package -n texlive-minitoc-doc
Summary:        Documentation for minitoc
Version:        svn48196
Provides:       tex-minitoc-doc
AutoReqProv:    No

%description -n texlive-minitoc-doc
Documentation for minitoc

%package -n texlive-minorrevision
Provides:       tex-minorrevision = %{tl_version}
License:        LPPL 1.2
Summary:        Quote and refer to a manuscript for minor revisions
Version:        svn32165.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(lineno.sty), tex(xr.sty)
Provides:       tex(minorrevision.sty) = %{tl_version}

%description -n texlive-minorrevision
The package supports those who publish articles in peer-
reviewed journals. In the final stages of the review process,
the authors typically have to provide an additional document
(such as a letter to the editors), in which they provide a list
of modifications that they made to the manuscript. The package
automatically provides line numbers and quotations from the
manuscript, for this letter. The package loads the package
lineno, so (in effect) shares lineno's incompatibilities.

%package -n texlive-minorrevision-doc
Summary:        Documentation for minorrevision
Version:        svn32165.1.1

Provides:       tex-minorrevision-doc
AutoReqProv:    No

%description -n texlive-minorrevision-doc
Documentation for minorrevision

%package -n texlive-minted
Provides:       tex-minted = %{tl_version}
License:        LPPL 1.3
Summary:        Highlighted source code for LaTeX
Version:        svn44855
Requires:       texlive-base, %{_bindir}/pygmentize, texlive-kpathsea-bin, tex-kpathsea, tex(keyval.sty)
Requires:       tex(kvoptions.sty), tex(fancyvrb.sty), tex(fvextra.sty), tex(ifthen.sty)
Requires:       tex(calc.sty), tex(ifplatform.sty), tex(pdftexcmds.sty), tex(etoolbox.sty)
Requires:       tex(xstring.sty), tex(lineno.sty), tex(xcolor.sty), tex(framed.sty)
Requires:       tex(newfloat.sty)
Provides:       tex(minted.sty) = %{tl_version}, tex(minted1.sty) = %{tl_version}

%description -n texlive-minted
The package that facilitates expressive syntax highlighting in
LaTeX using the powerful Pygments library. The package also
provides options to customize the highlighted source code
output using fancyvrb.

%package -n texlive-minted-doc
Summary:        Documentation for minted
Version:        svn44855
Provides:       tex-minted-doc
AutoReqProv:    No

%description -n texlive-minted-doc
Documentation for minted

%package -n texlive-minutes
Provides:       tex-minutes = %{tl_version}
License:        LPPL
Summary:        Typeset the minutes of meetings
Version:        svn42186
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(multicol.sty), tex(xspace.sty), tex(url.sty), tex(minitoc.sty)
Requires:       tex(keyval.sty)
Provides:       tex(minutes.sty) = %{tl_version}

%description -n texlive-minutes
Supports the creation of a collection of minutes. Features
include: Support of tasks (who, schedule, what, time of
finishing; possibility of creating a list of open tasks;
inclusion of open tasks from other minutes; Support for
attachments; Support of schedule dates (in planning: support
for the calendar package); Different versions ('secret parts');
and Macros for votes and decisions (list of decisions). Support
for minutes in German, Dutch and English is provided.

%package -n texlive-minutes-doc
Summary:        Documentation for minutes
Version:        svn42186
Provides:       tex-minutes-doc
AutoReqProv:    No

%description -n texlive-minutes-doc
Documentation for minutes

%package -n texlive-mla-paper
Provides:       tex-mla-paper = %{tl_version}
License:        LPPL
Summary:        Proper MLA formatting
Version:        svn20885.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mla.sty) = %{tl_version}

%description -n texlive-mla-paper
The package formats articles using the MLA style. The aim is
that students and other academics in the humanities should be
able to typeset their materials, properly, with minimal effort
on their part.

%package -n texlive-mla-paper-doc
Summary:        Documentation for mla-paper
Version:        svn20885.0

Provides:       tex-mla-paper-doc
AutoReqProv:    No

%description -n texlive-mla-paper-doc
Documentation for mla-paper

%package -n texlive-mlist
Provides:       tex-mlist = %{tl_version}
License:        LPPL
Summary:        Logical markup for lists
Version:        svn15878.0.6a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(ifmtarg.sty)
Provides:       tex(mlist.cfg) = %{tl_version}, tex(mlist.sty) = %{tl_version}

%description -n texlive-mlist
The package defines commands that create macros for typesetting
vectors, matrices and functions, in a logical way. For example,
logical indexing can then be used to refer to elements or
arguments without hard-coding the symbols in the document.

%package -n texlive-mlist-doc
Summary:        Documentation for mlist
Version:        svn15878.0.6a

Provides:       tex-mlist-doc
AutoReqProv:    No

%description -n texlive-mlist-doc
Documentation for mlist

%package -n texlive-mmap
Provides:       tex-mmap = %{tl_version}
License:        LPPL
Summary:        Include CMap resources in PDF files from PDFTeX
Version:        svn15878.1.03

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(cmap.sty), tex(ifpdf.sty)
Provides:       tex(mmap.sty) = %{tl_version}

%description -n texlive-mmap
The package is an extension of cmap with improved flexibility
and coverage, including the ability to re-encode Knuth's basic
mathematics fonts.

%package -n texlive-mmap-doc
Summary:        Documentation for mmap
Version:        svn15878.1.03

Provides:       tex-mmap-doc
AutoReqProv:    No

%description -n texlive-mmap-doc
Documentation for mmap

%package -n texlive-mnotes
Provides:       tex-mnotes = %{tl_version}
License:        LPPL 1.3
Summary:        Margin annotation for collaborative writing
Version:        svn35521.0.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(color.sty), tex(sidenotes.sty), tex(marginnote.sty)
Requires:       tex(tikz.sty), tex(ifoddpage.sty)
Provides:       tex(mnotes.sty) = %{tl_version}

%description -n texlive-mnotes
The package provides a flexible mechanism for annotating, and
commenting upon, collaboratively-written documents.

%package -n texlive-mnotes-doc
Summary:        Documentation for mnotes
Version:        svn35521.0.8

Provides:       tex-mnotes-doc
AutoReqProv:    No

%description -n texlive-mnotes-doc
Documentation for mnotes

%package -n texlive-mathcomp
Provides:       tex-mathcomp = %{tl_version}
License:        LPPL
Summary:        Text symbols in maths mode
Version:        svn15878.0.1f

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(textcomp.sty)
Provides:       tex(mathcomp.sty) = %{tl_version}

%description -n texlive-mathcomp
A package which provides access to some interesting characters
of the Text Companion fonts (TS1 encoding) in maths mode.

%package -n texlive-mathcomp-doc
Summary:        Documentation for mathcomp
Version:        svn15878.0.1f

Provides:       tex-mathcomp-doc
AutoReqProv:    No

%description -n texlive-mathcomp-doc
Documentation for mathcomp

%package -n texlive-mattens
Provides:       tex-mattens = %{tl_version}
License:        LPPL
Summary:        Matrices/tensor typesetting
Version:        svn17582.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty)
Provides:       tex(mattens.sty) = %{tl_version}

%description -n texlive-mattens
The mattens package contains the definitions to typeset
matrices, vectors and tensors as used in the engineering
community for the representation of common vectors and tensors
such as forces, velocities, moments of inertia, etc.

%package -n texlive-mattens-doc
Summary:        Documentation for mattens
Version:        svn17582.1.3

Provides:       tex-mattens-doc
AutoReqProv:    No

%description -n texlive-mattens-doc
Documentation for mattens

%package -n texlive-mhequ
Provides:       tex-mhequ = %{tl_version}
License:        Public Domain
Summary:        Multicolumn equations, tags, labels, sub-numbering
Version:        svn38224.1.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mhequ.sty) = %{tl_version}

%description -n texlive-mhequ
MHequ simplifies creating multi-column equation environments,
and tagging the equations therein. It supports sub-numbers of
blocks of equations (like (1.2a), (1.2b), etc) and references
to each equation individually (1.2a) or to the whole block
(1.2). The labels can be shown in draft mode. Comments in the
package itself describe usage.

%package -n texlive-mhequ-doc
Summary:        Documentation for mhequ
Version:        svn38224.1.7

Provides:       tex-mhequ-doc
AutoReqProv:    No

%description -n texlive-mhequ-doc
Documentation for mhequ

%package -n texlive-mcf2graph
Provides:       tex-mcf2graph = %{tl_version}
License:        BSD
Summary:        Draw chemical structure diagrams with Metafont/MetaPost
Version:        svn48046
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-mcf2graph
The Molecular Coding Format (MCF) is a linear notation for
describing chemical structure diagrams. This package converts
MCF to graphic files using Metafont / MetaPost.

%package -n texlive-mcf2graph-doc
Summary:        Documentation for mcf2graph
Version:        svn48046
Provides:       tex-mcf2graph-doc
AutoReqProv:    No

%description -n texlive-mcf2graph-doc
Documentation for mcf2graph

%package -n texlive-metago
Provides:       tex-metago = %{tl_version}
License:        LPPL
Summary:        MetaPost output of Go positions
Version:        svn15878.0.9
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-metago
The package allows you to draw Go game positions with MetaPost.
Two methods of usage are provided, either using the package
programmatically, or using the package via a script (which may
produce several images).

%package -n texlive-metago-doc
Summary:        Documentation for metago
Version:        svn15878.0.9

Provides:       tex-metago-doc
AutoReqProv:    No

%description -n texlive-metago-doc
Documentation for metago

%package -n texlive-metaobj
Provides:       tex-metaobj = %{tl_version}
License:        LPPL
Summary:        MetaPost package providing high-level objects
Version:        svn15878.0.93

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-metaobj
METAOBJ is a large metapost package providing high-level
objects. It implements many of PSTricks' features for node
connections, but also trees, matrices, and many other things.
It more or less contains boxes.mp and rboxes.mp. There is a
large (albeit not complete) documentation distributed with the
package. It is easily extensible with new objects.

%package -n texlive-metaobj-doc
Summary:        Documentation for metaobj
Version:        svn15878.0.93

Provides:       tex-metaobj-doc
AutoReqProv:    No

%description -n texlive-metaobj-doc
Documentation for metaobj

%package -n texlive-metaplot
Provides:       tex-metaplot = %{tl_version}
License:        LPPL
Summary:        Plot-manipulation macros for use in Metapost
Version:        svn15878.0.91

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-metaplot
MetaPlot is a set of Metapost macros for manipulating pre-
generated plots (and similar objects), and formatting them for
inclusion in a Metapost figure. The intent is that the plots
can be generated by some outside program, in an abstract manner
that does not require making decisions about on-page sizing and
layout, and then they can be imported into MetaPlot and
arranged using the full capabilities of Metapost. Metaplot also
includes a very flexible set of macros for generating plot
axes, which may be useful in other contexts as well. Presently,
MetaPlot is in something of a pre-release beta state; it is
quite functional, but the syntax of the commands is still
potentially in flux.

%package -n texlive-metaplot-doc
Summary:        Documentation for metaplot
Version:        svn15878.0.91

Provides:       tex-metaplot-doc
AutoReqProv:    No

%description -n texlive-metaplot-doc
Documentation for metaplot

%package -n texlive-metauml
Provides:       tex-metauml = %{tl_version}
License:        GPL+
Summary:        MetaPost library for typesetting UML diagrams
Version:        svn19692.0.2.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       metapost-metauml = %{tl_version}
Obsoletes:      metapost-metauml < %{tl_version}

%description -n texlive-metauml
MetaUML is a MetaPost library for typesetting UML diagrams,
which provides a usable, human-friendly textual notation for
UML, offering now support for class, package, activity, state,
and use case diagrams.

%package -n texlive-metauml-doc
Summary:        Documentation for metauml
Version:        svn19692.0.2.5

Provides:       tex-metauml-doc
AutoReqProv:    No

%description -n texlive-metauml-doc
Documentation for metauml

%package -n texlive-mfpic
Provides:       tex-mfpic = %{tl_version}
License:        LPPL 1.3
Summary:        Draw Metafont/post pictures from (La)TeX commands
Version:        svn28444.1.10

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty)
Provides:       tex(mfpic.sty) = %{tl_version}, tex(mfpic.tex) = %{tl_version}
Provides:       tex(mfpicdef.tex) = %{tl_version}

%description -n texlive-mfpic
Mfpic is a scheme for producing pictures from (La)TeX commands.
Commands \mfpic and \endmfpic (in LaTeX, the mfpic environment)
enclose a group in which drawing commands may be placed. The
commands generate a Meta-language file, which may be processed
by Metapost (or even Metafont). The resulting image file will
be read back in to the document to place the picture at the
point where the original (La)TeX commands appeared. Note that
the ability to use Metapost here means that the package works
equally well in LaTeX and PDFLaTeX.

%package -n texlive-mfpic-doc
Summary:        Documentation for mfpic
Version:        svn28444.1.10

Provides:       tex-mfpic-doc
AutoReqProv:    No

%description -n texlive-mfpic-doc
Documentation for mfpic

%package -n texlive-mfpic4ode
Provides:       tex-mfpic4ode = %{tl_version}
License:        LPPL
Summary:        Macros to draw direction fields and solutions of ODEs
Version:        svn17745.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mfpic4ode.sty) = %{tl_version}, tex(mfpic4ode.tex) = %{tl_version}

%description -n texlive-mfpic4ode
The package is a small set of macros for drawing direction
fields, phase portraits and trajectories of differential
equations and two dimensional autonomous systems. The Euler,
Runge-Kutta and 4th order Runge-Kutta algorithms are available
to solve the ODEs. The picture is translated into mfpic macros
and MetaPost is used to create the final drawing. The package
is was designed for use with LaTeX, but it can be used in plain
TeX as well. Online demonstration of the mfpic4ode macros is
available on the Mfpic Previewer as Example 6.

%package -n texlive-mfpic4ode-doc
Summary:        Documentation for mfpic4ode
Version:        svn17745.0.4

Provides:       tex-mfpic4ode-doc
AutoReqProv:    No

%description -n texlive-mfpic4ode-doc
Documentation for mfpic4ode

%package -n texlive-mkpattern
Provides:       tex-mkpattern = %{tl_version}
License:        LPPL
Summary:        A utility for making hyphenation patterns
Version:        svn15878.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mkpatter.tex) = %{tl_version}

%description -n texlive-mkpattern
Mkpattern is a general purpose program for the generation of
hyphenation patterns, with definition of letter sets and
template-like constructions. It also provides an easy way to
handle different input and output encodings, and featgures
generation of clean UTF-8 patterns. The package was used for
the creation of the Galician patterns.

%package -n texlive-mkpattern-doc
Summary:        Documentation for mkpattern
Version:        svn15878.1.2

Provides:       tex-mkpattern-doc
AutoReqProv:    No

%description -n texlive-mkpattern-doc
Documentation for mkpattern

%package -n texlive-makeplot
Provides:       tex-makeplot = %{tl_version}
License:        LPPL
Summary:        Easy plots from Matlab in LaTeX
Version:        svn15878.1.0.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fp.sty), tex(pst-plot.sty), tex(pstricks-add.sty), tex(xkeyval.sty)
Provides:       tex(makeplot.sty) = %{tl_version}

%description -n texlive-makeplot
Existing approaches to create EPS files from Matlab (laprint,
mma2ltx, print -eps, etc.) aren't satisfactory; makeplot aims
to resolve this problem. Makeplot is a LaTeX package that uses
the pstricks pst-plot functions to plot data that it takes from
Matlab output files.

%package -n texlive-makeplot-doc
Summary:        Documentation for makeplot
Version:        svn15878.1.0.6

Provides:       tex-makeplot-doc
AutoReqProv:    No

%description -n texlive-makeplot-doc
Documentation for makeplot

%package -n texlive-matc3
Provides:       tex-matc3 = %{tl_version}
License:        LPPL 1.3
Summary:        Commands for MatematicaC3 textbooks
Version:        svn29845.1.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(matc3.sty) = %{tl_version}

%description -n texlive-matc3
The package provides support for the Matematica C3 project to
produce free mathematical text books for use in Italian high
schools.

%package -n texlive-matc3-doc
Summary:        Documentation for matc3
Version:        svn29845.1.0.1

Provides:       tex-matc3-doc
AutoReqProv:    No

%description -n texlive-matc3-doc
Documentation for matc3

%package -n texlive-matc3mem
Provides:       tex-matc3mem = %{tl_version}
License:        LPPL 1.3
Summary:        Class for MatematicaC3 textbooks
Version:        svn35773.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsthm.sty), tex(xcolor.sty), tex(shadethm.sty)
Provides:       tex(matc3mem.cls) = %{tl_version}

%description -n texlive-matc3mem
The class is a development of memoir, with additions
(specifically, mathematical extensions) that provide support
for writing the books for the Matematica C3 project to produce
free mathematical textbooks for use in Italian high schools.

%package -n texlive-matc3mem-doc
Summary:        Documentation for matc3mem
Version:        svn35773.1.1

Provides:       tex-matc3mem-doc
AutoReqProv:    No

%description -n texlive-matc3mem-doc
Documentation for matc3mem

%package -n texlive-mcmthesis
Provides:       tex-mcmthesis = %{tl_version}
License:        LPPL 1.3
Summary:        Template designed for MCM/ICM
Version:        svn39515

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(etoolbox.sty), tex(fancyhdr.sty), tex(fancybox.sty)
Requires:       tex(ifthen.sty), tex(lastpage.sty), tex(listings.sty), tex(appendix.sty)
Requires:       tex(paralist.sty), tex(amsthm.sty), tex(amsfonts.sty), tex(amsmath.sty)
Requires:       tex(bm.sty), tex(amssymb.sty), tex(mathrsfs.sty), tex(latexsym.sty)
Requires:       tex(longtable.sty), tex(multirow.sty), tex(hhline.sty), tex(tabularx.sty)
Requires:       tex(array.sty), tex(flafter.sty), tex(pifont.sty), tex(calc.sty)
Requires:       tex(colortbl.sty), tex(booktabs.sty), tex(geometry.sty), tex(fontenc.sty)
Requires:       tex(berasans.sty), tex(hyperref.sty), tex(ifpdf.sty), tex(ifxetex.sty)
Requires:       tex(environ.sty), tex(graphicx.sty), tex(epstopdf.sty), tex(bmpsize.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(mcmthesis.cls) = %{tl_version}

%description -n texlive-mcmthesis
The package offers a template for MCM (The Mathematical Contest
in Modeling) and ICM (The Interdisciplinary Contest in
Modeling).

%package -n texlive-mcmthesis-doc
Summary:        Documentation for mcmthesis
Version:        svn39515

Provides:       tex-mcmthesis-doc
AutoReqProv:    No

%description -n texlive-mcmthesis-doc
Documentation for mcmthesis

%package -n texlive-mentis
Provides:       tex-mentis = %{tl_version}
License:        LPPL
Summary:        A basis for books to be published by Mentis publishers
Version:        svn15878.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontenc.sty), tex(babel.sty), tex(xspace.sty), tex(textcomp.sty)
Requires:       tex(scrpage2.sty), tex(jurabib.sty), tex(makeidx.sty), tex(relsize.sty)
Requires:       tex(microtype.sty), tex(multicol.sty), tex(ragged2e.sty), tex(geometry.sty)
Provides:       tex(mentis.cls) = %{tl_version}

%description -n texlive-mentis
This LaTeX class loads scrbook and provides changes necessary
for publishing at Mentis publishers in Paderborn, Germany. It
is not an official Mentis class, merely one developed by an
author in close co-operation with Mentis.

%package -n texlive-mentis-doc
Summary:        Documentation for mentis
Version:        svn15878.1.5

Provides:       tex-mentis-doc
AutoReqProv:    No

%description -n texlive-mentis-doc
Documentation for mentis

%package -n texlive-mnras
Provides:       tex-mnras = %{tl_version}
License:        LPPL 1.3
Summary:        Monthly Notices of the Royal Astronomical Society
Version:        svn37579.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mnras.cls) = %{tl_version}

%description -n texlive-mnras
Package for preparing papers in the journal Monthly Notices of
the Royal Astronomical Society.

%package -n texlive-mnras-doc
Summary:        Documentation for mnras
Version:        svn37579.3.0

Provides:       tex-mnras-doc
AutoReqProv:    No

%description -n texlive-mnras-doc
Documentation for mnras

%package -n texlive-matlab-prettifier
Provides:       tex-matlab-prettifier = %{tl_version}
License:        LPPL 1.3
Summary:        Pretty-print Matlab source code
Version:        svn34323.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(textcomp.sty), tex(xcolor.sty), tex(listings.sty)
Provides:       tex(matlab-prettifier.sty) = %{tl_version}

%description -n texlive-matlab-prettifier
The package extends the facilities of the listings package, to
pretty-print Matlab and Octave source code. (Note that support
of Octave syntax is not complete.)

%package -n texlive-matlab-prettifier-doc
Summary:        Documentation for matlab-prettifier
Version:        svn34323.0.3

Provides:       tex-matlab-prettifier-doc
AutoReqProv:    No

%description -n texlive-matlab-prettifier-doc
Documentation for matlab-prettifier

%package -n texlive-mhchem
Provides:       tex-mhchem = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset chemical formulae/equations and Risk and Safety phrases
Version:        svn48088
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(babel.sty), tex(twoopt.sty), tex(ifthen.sty), tex(textcomp.sty)
Requires:       tex(expl3.sty), tex(l3keys2e.sty), tex(l3regex.sty), tex(calc.sty)
Requires:       tex(amsmath.sty), tex(chemgreek.sty), tex(graphics.sty), tex(pgf.sty)
Requires:       tex(tikz.sty)
Provides:       tex(hpstatement.sty) = %{tl_version}, tex(mhchem.sty) = %{tl_version}
Provides:       tex(rsphrase.sty) = %{tl_version}

%description -n texlive-mhchem
The bundle provides three packages: The mhchem package provides
commands for typesetting chemical molecular formulae and
equations. The hpstatement package provides commands for the
official hazard statements and precautionary statements (H and
P statements) that are used to label chemicals. The rsphrase
package provides commands for the official Risk and Safety (R
and S) Phrases that are used to label chemicals. The package
requires the expl3 bundle.

%package -n texlive-mhchem-doc
Summary:        Documentation for mhchem
Version:        svn48088
Provides:       tex-mhchem-doc
AutoReqProv:    No

%description -n texlive-mhchem-doc
Documentation for mhchem

%package -n texlive-miller
Provides:       tex-miller = %{tl_version}
License:        LPPL
Summary:        Typeset miller indices
Version:        svn18789.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(miller.sty) = %{tl_version}

%description -n texlive-miller
Typeset miller indices, e.g., <1-20>, that are used in material
science with an easy syntax. Minus signs are printed as bar
above the corresponding number.

%package -n texlive-miller-doc
Summary:        Documentation for miller
Version:        svn18789.1.2

Provides:       tex-miller-doc
AutoReqProv:    No

%description -n texlive-miller-doc
Documentation for miller

%package -n texlive-mathspec
Provides:       tex-mathspec = %{tl_version}
License:        LPPL
Summary:        Specify arbitrary fonts for mathematics in XeTeX
Version:        svn42773
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etoolbox.sty), tex(amstext.sty), tex(ifxetex.sty), tex(fontspec.sty)
Requires:       tex(xkeyval.sty), tex(MnSymbol.sty)
Provides:       tex(mathspec.sty) = %{tl_version}

%description -n texlive-mathspec
The mathspec package provides an interface to typeset
mathematics in XeLaTeX with arbitrary text fonts using fontspec
as a backend. The package is under development and later
versions might to be incompatible with this version, as this
version is incompatible with earlier versions. The package
requires at least version 0.9995 of XeTeX.

%package -n texlive-mathspec-doc
Summary:        Documentation for mathspec
Version:        svn42773
Provides:       tex-mathspec-doc
AutoReqProv:    No

%description -n texlive-mathspec-doc
Documentation for mathspec

%package -n texlive-makebase-doc
Provides:       tex-makebase-doc = %{tl_version}
License:        LPPL
Summary:        doc files of makebase
Version:        svn41012

AutoReqProv:    No

%description -n texlive-makebase-doc
Documentation for makebase

%package -n texlive-makebase
Provides:       tex-makebase = %{tl_version}
License:        LPPL
Summary:        Typeset counters in a different base
Version:        svn41012

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(makebase.sty) = %{tl_version}

%description -n texlive-makebase
This package typesets a LaTeX counter such as page in an
arbitrary base (default 16). It does not change font or
typeface. The package extends the functionality of the existing
hex LaTeX 2.09 package and provides documentation. However, the
author is not a mathematician, and suggestions for rewriting
the code are welcomed. Warning: this is alpha software and may
contain bugs. Please report problems to the author.

%package -n texlive-markdown-doc
Provides:       tex-markdown-doc = %{tl_version}
License:        LPPL
Summary:        doc files of markdown
Version:        svn47397
AutoReqProv:    No

%description -n texlive-markdown-doc
Documentation for markdown

%package -n texlive-markdown
Provides:       tex-markdown = %{tl_version}
License:        LPPL
Summary:        A package for converting and rendering markdown documents inside TeX
Version:        svn47397
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(markdown.sty) = %{tl_version}, tex(markdown.tex) = %{tl_version}
Provides:       tex(t-markdown.tex) = %{tl_version}

%description -n texlive-markdown
The package provides facilities for the conversion of markdown
markup to plain TeX. These are provided both in form of a Lua
module and in form of plain TeX, LaTeX, and ConTeXt macro
packages that enable the direct inclusion of markdown documents
inside TeX documents. Architecturally, the package consists of
the Lunamark Lua module by John MacFarlane, which was slimmed
down and rewritten for the needs of the package. Lunamark
provides speedy markdown parsing for the rest of the package.
On top of Lunamark sits code for the plain TeX, LaTeX, and
ConTeXt formats by Vit Novotny.

%package -n texlive-mathpartir-doc
Provides:       tex-mathpartir-doc = %{tl_version}
License:        GPLv2+
Summary:        doc files of mathpartir
Version:        svn39864

AutoReqProv:    No

%description -n texlive-mathpartir-doc
Documentation for mathpartir

%package -n texlive-mathpartir
Provides:       tex-mathpartir = %{tl_version}
License:        GPLv2+
Summary:        Typesetting sequences of math formulas, e.g. type inference rules
Version:        svn39864

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mathpartir.sty) = %{tl_version}

%description -n texlive-mathpartir
The package provides macros for typesetting math formulas in
mixed horizontal and vertical mode, automatically as best fit.
It provides an environment mathpar that behaves much as a loose
centered paragraph where words are math formulas, and spaces
between them are larger and adjustable. It also provides a
macro \inferrule for typeseting fractions where both the
numerator and denominator may be sequences of formulas that
will be also typeset in a similar way. It can typically be used
for typeseting sets of type inference rules or typing
derivations. A macro inferrule for typesetting type inference
rules.

%package -n texlive-miama-doc
Provides:       tex-miama-doc = %{tl_version}
License:        LPPL and OFL
Summary:        doc files of miama
Version:        svn39837

AutoReqProv:    No

%description -n texlive-miama-doc
Documentation for miama

%package -n texlive-miama
Provides:       tex-miama = %{tl_version}
License:        LPPL and OFL
Summary:        The Miama Nueva handwriting font with LaTeX support
Version:        svn39837

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(miama.sty) = %{tl_version}, tex(miama.map) = %{tl_version}
Provides:       tex(lgrfmm.fd) = %{tl_version}, tex(ot1fmm.fd) = %{tl_version}
Provides:       tex(qxfmm.fd) = %{tl_version}, tex(x2fmm.fd) = %{tl_version}
Provides:       tex(t2cfmm.fd) = %{tl_version}, tex(t1fmm.fd) = %{tl_version}
Provides:       tex(t2afmm.fd) = %{tl_version}, tex(t5fmm.fd) = %{tl_version}
Provides:       tex(t2bfmm.fd) = %{tl_version}, tex(miama.pfb) = %{tl_version}
Provides:       tex(x2-miama.enc) = %{tl_version}, tex(t2b-miama.enc) = %{tl_version}
Provides:       tex(t2a-miama.enc) = %{tl_version}, tex(t1-miama.enc) = %{tl_version}
Provides:       tex(qx-miama.enc) = %{tl_version}, tex(t2c-miama.enc) = %{tl_version}
Provides:       tex(t5-miama.enc) = %{tl_version}, tex(lgr-miama.enc) = %{tl_version}
Provides:       tex(ot1-miama.enc) = %{tl_version}, tex(miama.otf) = %{tl_version}
Provides:       tex(miama-qx.tfm) = %{tl_version}, tex(miama-t2a.tfm) = %{tl_version}
Provides:       tex(miama-x2.tfm) = %{tl_version}, tex(miama-t1.tfm) = %{tl_version}
Provides:       tex(miama-ot1.tfm) = %{tl_version}, tex(miama-t2c.tfm) = %{tl_version}
Provides:       tex(miama-t5.tfm) = %{tl_version}, tex(miama-t2b.tfm) = %{tl_version}
Provides:       tex(miama-lgr.tfm) = %{tl_version}

%description -n texlive-miama
Miama Nueva is a handwriting / script font with over 1300
glyphs that supports latin, cyrillic, and greek. It comes
complete with LaTeX support.

%package -n texlive-maker
Summary:        Include Arduino or Processing code in LaTeX documents
Version:        svn44823
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(maker.sty) = %{tl_version}

%description -n texlive-maker
The first version of the package allows to include Arduino or
Processing code using three different forms: writing the code
directly in the LaTeX document writing Arduino or Processing
commands in line with the text calling to Arduino or Processing
files All these options support the syntax highlighting of the
oficial IDE.

%package -n texlive-marginfit
Summary:        Improved margin notes
Version:        svn48281
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(marginfit.sty) = %{tl_version}

%description -n texlive-marginfit
This package fixes various bugs with the margin paragraph
implementation of LaTeX. Those bugs include margin notes that
are attached to the wrong side as well as those that stick out
of the bottom of the page. This package provides a drop-in
replacement solution.

%package -n texlive-math-into-latex-4-doc
Summary:        Samples for the book `(More) Math into LaTeX', 4th edition.
Version:        svn44131
License:        Public Domain

%description -n texlive-math-into-latex-4-doc
Samples for the book `(More) Math into LaTeX', 4th edition.

%package -n texlive-mcexam
Summary:        LaTeX package for creating randomized Multiple Choice questions>
Version:        svn46155
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(mcexam.sty) = %{tl_version}

%description -n texlive-mcexam
LaTeX package for creating randomized Multiple Choice questions
The mcexam package is a LaTeX package that automatically
randomly permutes the order of questions and answer options in
different versions of a multiple choice exam/test. Next to the
exam versions themselves, the package also allows printing a
concept version of the exam, a key table with the correct
answers or points, and a document with solutions and
explanation per exam version. The package also allows writing
an R code which processes the results of the exam and
calculates the grades.

%package -n texlive-mendex-doc
Summary:        Docs for mendex
Version:        svn42767
License:        BSD

%description -n texlive-mendex-doc
This package provides documentation for Mendex (Japanese index
processor).

%package -n texlive-milog
Summary:        A LaTeX class for fulfilling the documentation duties according to the German minimum wage law MiLoG
Version:        svn41610
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(milog.cls) = %{tl_version}

%description -n texlive-milog
Seit dem 1. Januar 2015 gilt in Deutschland grundsatzlich fur
alle Arbeitnehmer ein flachendeckender gesetzlicher Mindestlohn
in Hohe von derzeit 8,50EUR pro Stunde. Mit Wirkung ab 1.
August 2015 wurden die Dokumentations- und
Aufzeichnungspflichten gelockert. Nach SS17 MiLoG, muss Beginn,
Ende und Dauer der taglichen Arbeitszeit der in SS22 MiLoG
definierten Arbeitnehmern (formlos) aufgezeichnet werden.
Zusatzlich ermoglicht milog.cls aus praktischen Grunden die
Aufzeichnug von unbezahlten Pausen und Bemerkungen (Ruhetag,
Urlaub, krank, ...). Die Erfassung der Arbeitszeiten erfolgt in
einer simplen CSV-Datei, aus der die Klasse automatisch einen
Arbeitszeitnachweis erstellt. Alternativ konnen die Daten auch
durch einen CSV-Export - mit eventueller Nachbearbeitung -
einer geeigneteten App erhoben werden. The milog.cls class
provides means to fulfill the documentation duties by the
German minimum wage law MiLoG. The recording of working hours
is carried out in a simple CSV file from which the class will
automatically create a time sheet. Alternatively, data can also
be collected by a CSV export of a suitable app.

%package -n texlive-missaali
Summary:        A late medieval OpenType textura font
Version:        svn42810
License:        OFL and LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(Missaali-Regular.otf) = %{tl_version}
Provides:       tex(missaali.sty) = %{tl_version}

%description -n texlive-missaali
This package contains the free OpenType Textura font Missaali
and a style file for using it with XeLaTeX. Textura is a
typeface based on the textus quadratus form of the textualis
formata that late medieval scribes used for the most valuable
manuscripts. The font Missaali is based on Textura that German
printer Bartholomew Ghotan used for printing missals and
psalters in the 1480s. This font has two intended use cases: as
a Gothic display font; and for emulating late-medieval
manuscripts. In addition to the basic textura letters, the font
contains a large number of abbreviation sigla as well as a set
of Lombardic initials. As modern typesetting algorithms are not
intended for creating 15th century style layout, the package
contains a XeLaTeX style file that makes it easier to achieve
the classic incunabula look.

%package -n texlive-mensa-tex
Summary:        Typeset simple school cafeteria menus
Version:        svn45997
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(array.sty)
Requires:       tex(colortbl.sty), tex(datetime2.sty), tex(datetime2-calc.sty), tex(geometry.sty)
Requires:       tex(graphicx.sty), tex(lmodern.sty), tex(textcomp.sty), tex(xcolor.sty)
Provides:       tex(mensa-tex.cls) = %{tl_version}

%description -n texlive-mensa-tex
This package provides a flexible LaTeX2e class for typesetting
school cafeteria menus consisting of two lunches (with
dessert), and dinner. It supports two different layouts: The
first layout is optimized for printing the menu on A4 paper.
The second layout is optimized for smartphone screens and uses
one (A6 sized) page per day. Supported localizations are
English (GB/US) and German. A way of defining additional
localizations is described in the documentation. The package
requires array, colortbl, datetime2, datetime2-calc, geometry,
graphicx, lmodern, textcomp, and xcolor.

%package -n texlive-manyind
Summary:        Provides support for many indexes
Version:        svn47574
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(manyind.sty) = %{tl_version}

%description -n texlive-manyind
This package provides support for many indexes, leaving all the
bookkeeping to LaTeX and makeindex. No extra programs or files
are needed. One runs latex and makeindex as if there is just
one index. In the main file one puts commands like
\setindex{main} to steer the flow. Some features of makeindex
may no longer work.

%package -n texlive-mathfam256
Summary:        Extend math family up to 256 for pLaTeX/upLaTeX/Lamed
Version:        svn46412
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(mathfam256.sty) = %{tl_version}

%description -n texlive-mathfam256
This package increases the upper limit of math symbols up to
256, using \omath... primitives. These primitives were
originally introduced in Omega and are currently available in
the following formats: pLaTeX (runs on e-pTeX), upLaTeX (runs
on e-upTeX), Lamed (runs on Aleph, successor of Omega).

%package -n texlive-mathfixs
Summary:        Fix various layout issues in math mode
Version:        svn46365
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(mathfixs.sty) = %{tl_version}

%description -n texlive-mathfixs
This is a LaTeX2e package to fix some odd behaviour in math
mode such as spacing around fractions and roots, math symbols
within bold text as well as capital Greek letters. It also adds
some related macros.

%package -n texlive-mathfont
Summary:        Use TrueType and OpenType fonts in math mode; compatible with XeTeX and LuaTeX
Version:        svn48329
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(mathfont.sty) = %{tl_version}

%description -n texlive-mathfont
The mathfont package provides a flexible interface for changing
the font of math mode characters. The package allows the user
to specify a default unicode font for each of six basic classes
of Latin and Greek characters, and it provides additional
support for unicode alphanumeric symbols. Crucially, mathfont
is compatible with both LuaLaTeX and XeLaTeX, and it provides
several font-loading commands that allow the user to change
fonts locally or for individual symbols within math mode.

%package -n texlive-mathpunctspace
Summary:        Control the space after punctuation in math expressions
Version:        svn46754
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(mathpunctspace.sty) = %{tl_version}

%description -n texlive-mathpunctspace
This package provides a mechanism to control the space after
commas and semicolons in mathematical expressions.

%package -n texlive-mgltex
Summary:        High-quality graphics from MGL scripts embedded in LaTeX documents
Version:        svn41676
License:        GPLv3
Requires:       texlive-base texlive-kpathsea
Provides:       tex(mgltex.sty) = %{tl_version}

%description -n texlive-mgltex
This package allows you to create high-quality
publication-ready graphics directly from MGL scripts embedded
into your LaTeX document, using the MathGL library. Besides
following the LaTeX philosophy of allowing you to concentrate
on content rather than output (mglTeX takes care of producing
the output), mglTeX facilitates the maintenance of your
document, since both code for text and code for plots are
contained in a single file. MathGL. is a fast and efficient
library by Alexey Balakin for the creation of high-quality
publication-ready scientific graphics. Although it defines
interfaces for many programming languages, it also implements
its own scripting language, called MGL, which can be used
independently.

%package -n texlive-milsymb
Summary:        LaTeX package for TikZ based drawing of military symbols as per NATO APP-6(C)
Version:        svn47482
License:        CC-BY-SA
Requires:       texlive-base texlive-kpathsea
Provides:       tex(milsymb.sty) = %{tl_version}

%description -n texlive-milsymb
The package offers commands to draw military symbols as per
NATO APP-6(C) https://www.awl.edu.pl/images/en/APP_6_C.pdf. It
has a set of commands for drawing all symbols found in the
document up to the control measures, as well as support for
custom non-standard symbols. Control measures are planned to be
included in a future release.

%package -n texlive-minidocument
Summary:        Creates miniature documents inside other LaTeX documents
Version:        svn43752
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(minidocument.sty) = %{tl_version}

%description -n texlive-minidocument
This package can be used to create miniature documents inside
other LaTeX documents. Inside the minidocument all features of
the outer vertical mode like page breaking, floats, marginpars,
etc. are available.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="arkandis/mintspirit public/mdsymbol public/mnsymbol"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-mflogo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mflogo/
%{_texdir}/texmf-dist/fonts/source/public/mflogo/
%{_texdir}/texmf-dist/fonts/tfm/public/mflogo/

%files -n texlive-mflogo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mflogo/

%files -n texlive-mfnfss
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mfnfss/

%files -n texlive-mfnfss-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mfnfss/

%files -n texlive-margbib
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/margbib/

%files -n texlive-margbib-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/margbib/

%files -n texlive-manfnt-font
%{_texdir}/texmf-dist/fonts/afm/hoekwater/manfnt-font/
%{_texdir}/texmf-dist/fonts/map/dvips/manfnt-font/
%{_texdir}/texmf-dist/fonts/type1/hoekwater/manfnt-font/

%files -n texlive-mflogo-font
%license knuth.txt
%{_texdir}/texmf-dist/fonts/afm/hoekwater/mflogo-font/
%{_texdir}/texmf-dist/fonts/map/dvips/mflogo-font/
%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo-font/

%files -n texlive-mflogo-font-doc
%license knuth.txt
%{_texdir}/texmf-dist/doc/fonts/mflogo-font/

%files -n texlive-mathabx
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/mathabx/
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/
%{_texdir}/texmf-dist/tex/generic/mathabx/

%files -n texlive-mathabx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/mathabx/

%files -n texlive-mathabx-type1
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/mathabx-type1/
%{_texdir}/texmf-dist/fonts/type1/public/mathabx-type1/

%files -n texlive-mathabx-type1-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/mathabx-type1/

%files -n texlive-mathdesign
%license gpl.txt
%{_texdir}/texmf-dist/dvips/mathdesign/
%{_texdir}/texmf-dist/fonts/enc/dvips/mathdesign/
%{_texdir}/texmf-dist/fonts/map/dvips/mathdesign/
%{_texdir}/texmf-dist/fonts/tfm/public/mathdesign/
%{_texdir}/texmf-dist/fonts/type1/public/mathdesign/
%{_texdir}/texmf-dist/fonts/vf/public/mathdesign/
%{_texdir}/texmf-dist/tex/latex/mathdesign/

%files -n texlive-mathdesign-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/mathdesign/

%files -n texlive-mdputu
%{_texdir}/texmf-dist/fonts/tfm/public/mdputu/
%{_texdir}/texmf-dist/fonts/vf/public/mdputu/
%{_texdir}/texmf-dist/tex/latex/mdputu/

%files -n texlive-mdputu-doc
%{_texdir}/texmf-dist/doc/latex/mdputu/

%files -n texlive-mdsymbol
%license ofl.txt
%{_datadir}/fonts/mdsymbol
%{_texdir}/texmf-dist/fonts/enc/dvips/mdsymbol/
%{_texdir}/texmf-dist/fonts/map/dvips/mdsymbol/
%{_texdir}/texmf-dist/fonts/opentype/public/mdsymbol/
%{_texdir}/texmf-dist/fonts/source/public/mdsymbol/
%{_texdir}/texmf-dist/fonts/tfm/public/mdsymbol/
%{_texdir}/texmf-dist/fonts/type1/public/mdsymbol/
%{_texdir}/texmf-dist/tex/latex/mdsymbol/

%files -n texlive-mdsymbol-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/mdsymbol/
%{_texdir}/texmf-dist/doc/latex/mdsymbol/

%files -n texlive-merriweather
%license ofl.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/merriweather/
%{_texdir}/texmf-dist/fonts/map/dvips/merriweather/
%{_texdir}/texmf-dist/fonts/tfm/sorkin/merriweather/
%{_texdir}/texmf-dist/fonts/truetype/sorkin/merriweather/
%{_texdir}/texmf-dist/fonts/type1/sorkin/merriweather/
%{_texdir}/texmf-dist/fonts/vf/sorkin/merriweather/
%{_texdir}/texmf-dist/tex/latex/merriweather/

%files -n texlive-merriweather-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/merriweather/

%files -n texlive-mintspirit
%license ofl.txt
%{_datadir}/fonts/mintspirit
%{_texdir}/texmf-dist/fonts/enc/dvips/mintspirit/
%{_texdir}/texmf-dist/fonts/map/dvips/mintspirit/
%{_texdir}/texmf-dist/fonts/opentype/arkandis/mintspirit/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/mintspirit/
%{_texdir}/texmf-dist/fonts/type1/arkandis/mintspirit/
%{_texdir}/texmf-dist/fonts/vf/arkandis/mintspirit/
%{_texdir}/texmf-dist/tex/latex/mintspirit/

%files -n texlive-mintspirit-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/mintspirit/

%files -n texlive-mnsymbol
%license pd.txt
%{_datadir}/fonts/mnsymbol
%{_texdir}/texmf-dist/fonts/enc/dvips/mnsymbol/
%{_texdir}/texmf-dist/fonts/map/dvips/mnsymbol/
%{_texdir}/texmf-dist/fonts/map/vtex/mnsymbol/
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/
%{_texdir}/texmf-dist/tex/latex/mnsymbol/

%files -n texlive-mnsymbol-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/mnsymbol/

%files -n texlive-marvosym
%license ofl.txt
%{_texdir}/texmf-dist/fonts/afm/public/marvosym/
%{_texdir}/texmf-dist/fonts/map/dvips/marvosym/
%{_texdir}/texmf-dist/fonts/tfm/public/marvosym/
%{_texdir}/texmf-dist/fonts/truetype/public/marvosym/
%{_texdir}/texmf-dist/fonts/type1/public/marvosym/
%{_texdir}/texmf-dist/tex/latex/marvosym/

%files -n texlive-marvosym-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/marvosym/

%files -n texlive-mathpazo
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/mathpazo/
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/
%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/
%{_texdir}/texmf-dist/fonts/vf/public/mathpazo/

%files -n texlive-mathpazo-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/mathpazo/

%files -n texlive-mathdots
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/mathdots/

%files -n texlive-mathdots-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/mathdots/

%files -n texlive-metatex
%license gpl.txt
%{_texdir}/texmf-dist/tex/plain/metatex/

%files -n texlive-metatex-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/plain/metatex/

%files -n texlive-midnight
%{_texdir}/texmf-dist/tex/generic/midnight/

%files -n texlive-midnight-doc
%{_texdir}/texmf-dist/doc/generic/midnight/

%files -n texlive-metrix
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/metrix/

%files -n texlive-metrix-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/metrix/

%files -n texlive-macros2e-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/macros2e/

%files -n texlive-math-e-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/math-e/

%files -n texlive-maths-symbols-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/maths-symbols/

%files -n texlive-memdesign-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/memdesign/

%files -n texlive-metafont-beginners-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/metafont-beginners/

%files -n texlive-metapost-examples-doc
%{_texdir}/texmf-dist/doc/metapost/metapost-examples/

%files -n texlive-mafr
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/mafr/

%files -n texlive-mafr-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/mafr/

%files -n texlive-microtype-de-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/microtype-de/

%files -n texlive-memoir
%license lppl1.3.txt
%{_texdir}/texmf-dist/makeindex/memoir/
%{_texdir}/texmf-dist/tex/latex/memoir/

%files -n texlive-memoir-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/memoir/

%files -n texlive-mathtools
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mathtools/

%files -n texlive-mathtools-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mathtools/

%files -n texlive-mdwtools
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/mdwtools/

%files -n texlive-mdwtools-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/mdwtools/

%files -n texlive-metalogo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/metalogo/

%files -n texlive-metalogo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/metalogo/

%files -n texlive-microtype
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/microtype/

%files -n texlive-microtype-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/microtype/

%files -n texlive-makeshape
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/makeshape/

%files -n texlive-makeshape-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/makeshape/

%files -n texlive-miniplot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/miniplot/

%files -n texlive-miniplot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/miniplot/

%files -n texlive-macroswap
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/macroswap/

%files -n texlive-macroswap-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/macroswap/

%files -n texlive-magaz
%{_texdir}/texmf-dist/tex/latex/magaz/

%files -n texlive-magaz-doc
%{_texdir}/texmf-dist/doc/latex/magaz/

%files -n texlive-mailing
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mailing/

%files -n texlive-mailing-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mailing/

%files -n texlive-mailmerge
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/mailmerge/

%files -n texlive-mailmerge-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/mailmerge/

%files -n texlive-makebarcode
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/makebarcode/

%files -n texlive-makebarcode-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/makebarcode/

%files -n texlive-makebox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/makebox/

%files -n texlive-makebox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/makebox/

%files -n texlive-makecell
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/makecell/

%files -n texlive-makecell-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/makecell/

%files -n texlive-makecirc
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/makecirc/

%files -n texlive-makecirc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/makecirc/

%files -n texlive-makecmds
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/makecmds/

%files -n texlive-makecmds-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/makecmds/

%files -n texlive-makeglos
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/makeglos/

%files -n texlive-makeglos-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/makeglos/

%files -n texlive-mandi
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mandi/

%files -n texlive-mandi-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mandi/

%files -n texlive-manfnt
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/manfnt/

%files -n texlive-manuscript
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/manuscript/

%files -n texlive-manuscript-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/manuscript/

%files -n texlive-marginfix
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/marginfix/

%files -n texlive-marginfix-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/marginfix/

%files -n texlive-marginnote
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/marginnote/

%files -n texlive-marginnote-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/marginnote/

%files -n texlive-mathalfa
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mathalfa/

%files -n texlive-mathalfa-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mathalfa/

%files -n texlive-mathastext
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mathastext/

%files -n texlive-mathastext-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mathastext/

%files -n texlive-mathexam
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mathexam/

%files -n texlive-mathexam-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mathexam/

%files -n texlive-maybemath
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/maybemath/

%files -n texlive-maybemath-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/maybemath/

%files -n texlive-mbenotes
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/mbenotes/

%files -n texlive-mbenotes-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/mbenotes/

%files -n texlive-mcaption
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mcaption/

%files -n texlive-mcaption-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mcaption/

%files -n texlive-mceinleger
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/mceinleger/

%files -n texlive-mceinleger-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/mceinleger/

%files -n texlive-mcite
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/mcite/

%files -n texlive-mcite-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/mcite/

%files -n texlive-mciteplus
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/mciteplus/
%{_texdir}/texmf-dist/tex/latex/mciteplus/

%files -n texlive-mciteplus-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mciteplus/

%files -n texlive-mdframed
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mdframed/

%files -n texlive-mdframed-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mdframed/

%files -n texlive-media9
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/media9/

%files -n texlive-media9-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/media9/

%files -n texlive-medstarbeamer
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/medstarbeamer/

%files -n texlive-medstarbeamer-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/medstarbeamer/

%files -n texlive-meetingmins
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/meetingmins/

%files -n texlive-meetingmins-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/meetingmins/

%files -n texlive-memexsupp
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/memexsupp/

%files -n texlive-memexsupp-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/memexsupp/

%files -n texlive-memory
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/memory/

%files -n texlive-memory-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/memory/

%files -n texlive-menu
%{_texdir}/texmf-dist/tex/latex/menu/

%files -n texlive-menu-doc
%{_texdir}/texmf-dist/doc/latex/menu/

%files -n texlive-menukeys
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/menukeys/

%files -n texlive-menukeys-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/menukeys/

%files -n texlive-method
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/method/

%files -n texlive-method-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/method/

%files -n texlive-metre
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/metre/

%files -n texlive-metre-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/metre/

%files -n texlive-mfirstuc
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/mfirstuc/
%{_texdir}/texmf-dist/tex/latex/mfirstuc/

%files -n texlive-mfirstuc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mfirstuc/

%files -n texlive-mftinc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mftinc/

%files -n texlive-mftinc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mftinc/

%files -n texlive-midpage
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/midpage/

%files -n texlive-midpage-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/midpage/

%files -n texlive-minibox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/minibox/

%files -n texlive-minibox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/minibox/

%files -n texlive-minifp
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/minifp/

%files -n texlive-minifp-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/minifp/

%files -n texlive-minipage-marginpar
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/minipage-marginpar/

%files -n texlive-minipage-marginpar-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/minipage-marginpar/

%files -n texlive-minitoc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/minitoc/

%files -n texlive-minitoc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/minitoc/

%files -n texlive-minorrevision
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/minorrevision/

%files -n texlive-minorrevision-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/minorrevision/

%files -n texlive-minted
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/minted/

%files -n texlive-minted-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/minted/

%files -n texlive-minutes
%{_texdir}/texmf-dist/tex/latex/minutes/

%files -n texlive-minutes-doc
%{_texdir}/texmf-dist/doc/latex/minutes/

%files -n texlive-mla-paper
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mla-paper/

%files -n texlive-mla-paper-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mla-paper/

%files -n texlive-mlist
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mlist/

%files -n texlive-mlist-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mlist/

%files -n texlive-mmap
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mmap/

%files -n texlive-mmap-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mmap/

%files -n texlive-mnotes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mnotes/

%files -n texlive-mnotes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mnotes/

%files -n texlive-mathcomp
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mathcomp/

%files -n texlive-mathcomp-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mathcomp/

%files -n texlive-mattens
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mattens/

%files -n texlive-mattens-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mattens/

%files -n texlive-mhequ
%{_texdir}/texmf-dist/tex/latex/mhequ/

%files -n texlive-mhequ-doc
%{_texdir}/texmf-dist/doc/latex/mhequ/

%files -n texlive-mcf2graph
%license bsd.txt
%{_texdir}/texmf-dist/metapost/mcf2graph/

%files -n texlive-mcf2graph-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/metapost/mcf2graph/

%files -n texlive-metago
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/metago/

%files -n texlive-metago-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/metago/

%files -n texlive-metaobj
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/metaobj/

%files -n texlive-metaobj-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/metaobj/

%files -n texlive-metaplot
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/metaplot/

%files -n texlive-metaplot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/metaplot/

%files -n texlive-metauml
%license gpl.txt
%{_texdir}/texmf-dist/metapost/metauml/

%files -n texlive-metauml-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/metapost/metauml/

%files -n texlive-mfpic
%license lppl1.3.txt
%{_texdir}/texmf-dist/metafont/mfpic/
%{_texdir}/texmf-dist/metapost/mfpic/
%{_texdir}/texmf-dist/tex/generic/mfpic/

%files -n texlive-mfpic-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/mfpic/

%files -n texlive-mfpic4ode
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mfpic4ode/

%files -n texlive-mfpic4ode-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mfpic4ode/

%files -n texlive-mkpattern
%license lppl1.txt
%{_texdir}/texmf-dist/tex/plain/mkpattern/

%files -n texlive-mkpattern-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/plain/mkpattern/

%files -n texlive-makeplot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/makeplot/

%files -n texlive-makeplot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/makeplot/

%files -n texlive-matc3
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/matc3/

%files -n texlive-matc3-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/matc3/

%files -n texlive-matc3mem
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/matc3mem/

%files -n texlive-matc3mem-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/matc3mem/

%files -n texlive-mcmthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mcmthesis/

%files -n texlive-mcmthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mcmthesis/

%files -n texlive-mentis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mentis/

%files -n texlive-mentis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mentis/

%files -n texlive-mnras
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/mnras/
%{_texdir}/texmf-dist/tex/latex/mnras/

%files -n texlive-mnras-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mnras/

%files -n texlive-matlab-prettifier
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/matlab-prettifier/

%files -n texlive-matlab-prettifier-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/matlab-prettifier/

%files -n texlive-mhchem
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mhchem/

%files -n texlive-mhchem-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mhchem/

%files -n texlive-miller
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/miller/

%files -n texlive-miller-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/miller/

%files -n texlive-mathspec
%license lppl1.txt
%{_texdir}/texmf-dist/tex/xelatex/mathspec/

%files -n texlive-mathspec-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/xelatex/mathspec/

%files -n texlive-makebase-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/makebase/

%files -n texlive-makebase
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/makebase/

%files -n texlive-markdown-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/markdown/
%{_texdir}/texmf-dist/doc/context/third/markdown/
%{_texdir}/texmf-dist/doc/latex/markdown/

%files -n texlive-markdown
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/markdown/
%{_texdir}/texmf-dist/tex/latex/markdown/
%{_texdir}/texmf-dist/tex/luatex/markdown/
%{_texdir}/texmf-dist/tex/context/third/markdown/
%{_texdir}/texmf-dist/scripts/markdown/markdown-cli.lua

%files -n texlive-mathpartir-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/mathpartir/

%files -n texlive-mathpartir
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/mathpartir/

%files -n texlive-miama-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/miama/

%files -n texlive-miama
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/miama/
%{_texdir}/texmf-dist/fonts/opentype/public/miama/
%{_texdir}/texmf-dist/fonts/map/dvips/miama/
%{_texdir}/texmf-dist/fonts/tfm/public/miama/
%{_texdir}/texmf-dist/fonts/enc/dvips/miama/
%{_texdir}/texmf-dist/fonts/afm/public/miama/
%{_texdir}/texmf-dist/fonts/type1/public/miama/

%files -n texlive-maker
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/maker/
%{_texdir}/texmf-dist/tex/latex/maker/

%files -n texlive-marginfit
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/marginfit/
%{_texdir}/texmf-dist/tex/latex/marginfit/

%files -n texlive-math-into-latex-4-doc
%doc %{_texdir}/texmf-dist/doc/latex/math-into-latex-4/

%files -n texlive-mcexam
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/mcexam/
%{_texdir}/texmf-dist/tex/latex/mcexam/

%files -n texlive-mendex-doc
%doc %{_texdir}/texmf-dist/doc/support/mendex/

%files -n texlive-milog
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/latex/milog/
%{_texdir}/texmf-dist/tex/latex/milog/

%files -n texlive-missaali
%license ofl.txt lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/fonts/missaali/
%{_texdir}/texmf-dist/fonts/opentype/public/missaali/
%{_texdir}/texmf-dist/tex/latex/missaali/

%files -n texlive-mensa-tex
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mensa-tex/
%doc %{_texdir}/texmf-dist/doc/latex/mensa-tex/

%files -n texlive-manyind
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/manyind/
%doc %{_texdir}/texmf-dist/doc/latex/manyind/

%files -n texlive-mathfam256
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/mathfam256/
%doc %{_texdir}/texmf-dist/doc/latex/mathfam256/

%files -n texlive-mathfixs
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/mathfixs/
%doc %{_texdir}/texmf-dist/doc/latex/mathfixs/

%files -n texlive-mathfont
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/mathfont/
%doc %{_texdir}/texmf-dist/doc/latex/mathfont/

%files -n texlive-mathpunctspace
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/mathpunctspace/
%doc %{_texdir}/texmf-dist/doc/latex/mathpunctspace/

%files -n texlive-mgltex
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/mgltex/
%doc %{_texdir}/texmf-dist/doc/latex/mgltex/

%files -n texlive-milsymb
%{_texdir}/texmf-dist/tex/latex/milsymb/
%doc %{_texdir}/texmf-dist/doc/latex/milsymb/

%files -n texlive-minidocument
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/minidocument/
%doc %{_texdir}/texmf-dist/doc/latex/minidocument/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
