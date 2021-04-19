"""
    pygments.lexers.foxpro
    ~~~~~~~~~~~~~~~~~~~~~~

    Simple lexer for Microsoft Visual FoxPro source code.

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer
from pygments.token import Punctuation, Text, Comment, Operator, Keyword, \
     Name, String

__all__ = ['FoxProLexer']


class FoxProLexer(RegexLexer):
    """Lexer for Microsoft Visual FoxPro language.

    FoxPro syntax allows to shorten all keywords and function names
    to 4 characters.  Shortened forms are not recognized by this lexer.

    .. versionadded:: 1.6
    """

    name = 'FoxPro'
    aliases = ['foxpro', 'vfp', 'clipper', 'xbase']
    filenames = ['*.PRG', '*.prg']
    mimetype = []

    flags = re.IGNORECASE | re.MULTILINE

    tokens = {
        'root': [
            (r';\s*\n', Punctuation),  # consume newline
            (r'(^|\n)\s*', Text, 'newline'),

            # Square brackets may be used for array indices
            # and for string literal.  Look for arrays
            # before matching string literals.
            (r'(?<=\w)\[[0-9, ]+\]', Text),
            (r'\'[^\'\n]*\'|"[^"\n]*"|\[[^]*]\]', String),
            (r'(^\s*\*|&&|&amp;&amp;).*?\n', Comment.Single),

            (r'(ABS|ACLASS|ACOPY|ACOS|ADATABASES|ADBOBJECTS|ADDBS|'
             r'ADDPROPERTY|ADEL|ADIR|ADLLS|ADOCKSTATE|AELEMENT|AERROR|'
             r'AEVENTS|AFIELDS|AFONT|AGETCLASS|AGETFILEVERSION|AINS|'
             r'AINSTANCE|ALANGUAGE|ALEN|ALIAS|ALINES|ALLTRIM|'
             r'AMEMBERS|AMOUSEOBJ|ANETRESOURCES|APRINTERS|APROCINFO|'
             r'ASC|ASCAN|ASELOBJ|ASESSIONS|ASIN|ASORT|ASQLHANDLES|'
             r'ASTACKINFO|ASUBSCRIPT|AT|AT_C|ATAGINFO|ATAN|ATC|ATCC|'
             r'ATCLINE|ATLINE|ATN2|AUSED|AVCXCLASSES|BAR|BARCOUNT|'
             r'BARPROMPT|BETWEEN|BINDEVENT|BINTOC|BITAND|BITCLEAR|'
             r'BITLSHIFT|BITNOT|BITOR|BITRSHIFT|BITSET|BITTEST|BITXOR|'
             r'BOF|CANDIDATE|CAPSLOCK|CAST|CDOW|CDX|CEILING|CHR|CHRSAW|'
             r'CHRTRAN|CHRTRANC|CLEARRESULTSET|CMONTH|CNTBAR|CNTPAD|COL|'
             r'COM|Functions|COMARRAY|COMCLASSINFO|COMPOBJ|COMPROP|'
             r'COMRETURNERROR|COS|CPCONVERT|CPCURRENT|CPDBF|CREATEBINARY|'
             r'CREATEOBJECT|CREATEOBJECTEX|CREATEOFFLINE|CTOBIN|CTOD|'
             r'CTOT|CURDIR|CURSORGETPROP|CURSORSETPROP|CURSORTOXML|'
             r'CURVAL|DATE|DATETIME|DAY|DBC|DBF|DBGETPROP|DBSETPROP|'
             r'DBUSED|DDEAbortTrans|DDEAdvise|DDEEnabled|DDEExecute|'
             r'DDEInitiate|DDELastError|DDEPoke|DDERequest|DDESetOption|'
             r'DDESetService|DDESetTopic|DDETerminate|DEFAULTEXT|'
             r'DELETED|DESCENDING|DIFFERENCE|DIRECTORY|DISKSPACE|'
             r'DisplayPath|DMY|DODEFAULT|DOW|DRIVETYPE|DROPOFFLINE|'
             r'DTOC|DTOR|DTOS|DTOT|EDITSOURCE|EMPTY|EOF|ERROR|EVAL(UATE)?|'
             r'EVENTHANDLER|EVL|EXECSCRIPT|EXP|FCHSIZE|FCLOSE|FCOUNT|'
             r'FCREATE|FDATE|FEOF|FERROR|FFLUSH|FGETS|FIELD|FILE|'
             r'FILETOSTR|FILTER|FKLABEL|FKMAX|FLDLIST|FLOCK|FLOOR|'
             r'FONTMETRIC|FOPEN|FOR|FORCEEXT|FORCEPATH|FOUND|FPUTS|'
             r'FREAD|FSEEK|FSIZE|FTIME|FULLPATH|FV|FWRITE|'
             r'GETAUTOINCVALUE|GETBAR|GETCOLOR|GETCP|GETDIR|GETENV|'
             r'GETFILE|GETFLDSTATE|GETFONT|GETINTERFACE|'
             r'GETNEXTMODIFIED|GETOBJECT|GETPAD|GETPEM|GETPICT|'
             r'GETPRINTER|GETRESULTSET|GETWORDCOUNT|GETWORDNUM|'
             r'GETCURSORADAPTER|GOMONTH|HEADER|HOME|HOUR|ICASE|'
             r'IDXCOLLATE|IIF|IMESTATUS|INDBC|INDEXSEEK|INKEY|INLIST|'
             r'INPUTBOX|INSMODE|INT|ISALPHA|ISBLANK|ISCOLOR|ISDIGIT|'
             r'ISEXCLUSIVE|ISFLOCKED|ISLEADBYTE|ISLOWER|ISMEMOFETCHED|'
             r'ISMOUSE|ISNULL|ISPEN|ISREADONLY|ISRLOCKED|'
             r'ISTRANSACTABLE|ISUPPER|JUSTDRIVE|JUSTEXT|JUSTFNAME|'
             r'JUSTPATH|JUSTSTEM|KEY|KEYMATCH|LASTKEY|LEFT|LEFTC|LEN|'
             r'LENC|LIKE|LIKEC|LINENO|LOADPICTURE|LOCFILE|LOCK|LOG|'
             r'LOG10|LOOKUP|LOWER|LTRIM|LUPDATE|MAKETRANSACTABLE|MAX|'
             r'MCOL|MDOWN|MDX|MDY|MEMLINES|MEMORY|MENU|MESSAGE|'
             r'MESSAGEBOX|MIN|MINUTE|MLINE|MOD|MONTH|MRKBAR|MRKPAD|'
             r'MROW|MTON|MWINDOW|NDX|NEWOBJECT|NORMALIZE|NTOM|NUMLOCK|'
             r'NVL|OBJNUM|OBJTOCLIENT|OBJVAR|OCCURS|OEMTOANSI|OLDVAL|'
             r'ON|ORDER|OS|PAD|PADL|PARAMETERS|PAYMENT|PCOL|PCOUNT|'
             r'PEMSTATUS|PI|POPUP|PRIMARY|PRINTSTATUS|PRMBAR|PRMPAD|'
             r'PROGRAM|PROMPT|PROPER|PROW|PRTINFO|PUTFILE|PV|QUARTER|'
             r'RAISEEVENT|RAND|RAT|RATC|RATLINE|RDLEVEL|READKEY|RECCOUNT|'
             r'RECNO|RECSIZE|REFRESH|RELATION|REPLICATE|REQUERY|RGB|'
             r'RGBSCHEME|RIGHT|RIGHTC|RLOCK|ROUND|ROW|RTOD|RTRIM|'
             r'SAVEPICTURE|SCHEME|SCOLS|SEC|SECONDS|SEEK|SELECT|SET|'
             r'SETFLDSTATE|SETRESULTSET|SIGN|SIN|SKPBAR|SKPPAD|SOUNDEX|'
             r'SPACE|SQLCANCEL|SQLCOLUMNS|SQLCOMMIT|SQLCONNECT|'
             r'SQLDISCONNECT|SQLEXEC|SQLGETPROP|SQLIDLEDISCONNECT|'
             r'SQLMORERESULTS|SQLPREPARE|SQLROLLBACK|SQLSETPROP|'
             r'SQLSTRINGCONNECT|SQLTABLES|SQRT|SROWS|STR|STRCONV|'
             r'STREXTRACT|STRTOFILE|STRTRAN|STUFF|STUFFC|SUBSTR|'
             r'SUBSTRC|SYS|SYSMETRIC|TABLEREVERT|TABLEUPDATE|TAG|'
             r'TAGCOUNT|TAGNO|TAN|TARGET|TEXTMERGE|TIME|TRANSFORM|'
             r'TRIM|TTOC|TTOD|TXNLEVEL|TXTWIDTH|TYPE|UNBINDEVENTS|'
             r'UNIQUE|UPDATED|UPPER|USED|VAL|VARREAD|VARTYPE|VERSION|'
             r'WBORDER|WCHILD|WCOLS|WDOCKABLE|WEEK|WEXIST|WFONT|WLAST|'
             r'WLCOL|WLROW|WMAXIMUM|WMINIMUM|WONTOP|WOUTPUT|WPARENT|'
             r'WREAD|WROWS|WTITLE|WVISIBLE|XMLTOCURSOR|XMLUPDATEGRAM|'
             r'YEAR)(?=\s*\()', Name.Function),

            (r'_ALIGNMENT|_ASCIICOLS|_ASCIIROWS|_ASSIST|_BEAUTIFY|_BOX|'
             r'_BROWSER|_BUILDER|_CALCMEM|_CALCVALUE|_CLIPTEXT|_CONVERTER|'
             r'_COVERAGE|_CUROBJ|_DBLCLICK|_DIARYDATE|_DOS|_FOXDOC|_FOXREF|'
             r'_GALLERY|_GENGRAPH|_GENHTML|_GENMENU|_GENPD|_GENSCRN|'
             r'_GENXTAB|_GETEXPR|_INCLUDE|_INCSEEK|_INDENT|_LMARGIN|_MAC|'
             r'_MENUDESIGNER|_MLINE|_PADVANCE|_PAGENO|_PAGETOTAL|_PBPAGE|'
             r'_PCOLNO|_PCOPIES|_PDRIVER|_PDSETUP|_PECODE|_PEJECT|_PEPAGE|'
             r'_PLENGTH|_PLINENO|_PLOFFSET|_PPITCH|_PQUALITY|_PRETEXT|'
             r'_PSCODE|_PSPACING|_PWAIT|_RMARGIN|_REPORTBUILDER|'
             r'_REPORTOUTPUT|_REPORTPREVIEW|_SAMPLES|_SCCTEXT|_SCREEN|'
             r'_SHELL|_SPELLCHK|_STARTUP|_TABS|_TALLY|_TASKPANE|_TEXT|'
             r'_THROTTLE|_TOOLBOX|_TOOLTIPTIMEOUT|_TRANSPORT|_TRIGGERLEVEL|'
             r'_UNIX|_VFP|_WINDOWS|_WIZARD|_WRAP', Keyword.Pseudo),

            (r'THISFORMSET|THISFORM|THIS', Name.Builtin),

            (r'Application|CheckBox|Collection|Column|ComboBox|'
             r'CommandButton|CommandGroup|Container|Control|CursorAdapter|'
             r'Cursor|Custom|DataEnvironment|DataObject|EditBox|'
             r'Empty|Exception|Fields|Files|File|FormSet|Form|FoxCode|'
             r'Grid|Header|Hyperlink|Image|Label|Line|ListBox|Objects|'
             r'OptionButton|OptionGroup|PageFrame|Page|ProjectHook|Projects|'
             r'Project|Relation|ReportListener|Separator|Servers|Server|'
             r'Session|Shape|Spinner|Tables|TextBox|Timer|ToolBar|'
             r'XMLAdapter|XMLField|XMLTable', Name.Class),

            (r'm\.[a-z_]\w*', Name.Variable),
            (r'\.(F|T|AND|OR|NOT|NULL)\.|\b(AND|OR|NOT|NULL)\b', Operator.Word),

            (r'\.(ActiveColumn|ActiveControl|ActiveForm|ActivePage|'
             r'ActiveProject|ActiveRow|AddLineFeeds|ADOCodePage|Alias|'
             r'Alignment|Align|AllowAddNew|AllowAutoColumnFit|'
             r'AllowCellSelection|AllowDelete|AllowHeaderSizing|'
             r'AllowInsert|AllowModalMessages|AllowOutput|AllowRowSizing|'
             r'AllowSimultaneousFetch|AllowTabs|AllowUpdate|'
             r'AlwaysOnBottom|AlwaysOnTop|Anchor|Application|'
             r'AutoActivate|AutoCenter|AutoCloseTables|AutoComplete|'
             r'AutoCompSource|AutoCompTable|AutoHideScrollBar|'
             r'AutoIncrement|AutoOpenTables|AutoRelease|AutoSize|'
             r'AutoVerbMenu|AutoYield|BackColor|ForeColor|BackStyle|'
             r'BaseClass|BatchUpdateCount|BindControls|BorderColor|'
             r'BorderStyle|BorderWidth|BoundColumn|BoundTo|Bound|'
             r'BreakOnError|BufferModeOverride|BufferMode|'
             r'BuildDateTime|ButtonCount|Buttons|Cancel|Caption|'
             r'Centered|Century|ChildAlias|ChildOrder|ChildTable|'
             r'ClassLibrary|Class|ClipControls|Closable|CLSID|CodePage|'
             r'ColorScheme|ColorSource|ColumnCount|ColumnLines|'
             r'ColumnOrder|Columns|ColumnWidths|CommandClauses|'
             r'Comment|CompareMemo|ConflictCheckCmd|ConflictCheckType|'
             r'ContinuousScroll|ControlBox|ControlCount|Controls|'
             r'ControlSource|ConversionFunc|Count|CurrentControl|'
             r'CurrentDataSession|CurrentPass|CurrentX|CurrentY|'
             r'CursorSchema|CursorSource|CursorStatus|Curvature|'
             r'Database|DataSessionID|DataSession|DataSourceType|'
             r'DataSource|DataType|DateFormat|DateMark|Debug|'
             r'DeclareXMLPrefix|DEClassLibrary|DEClass|DefaultFilePath|'
             r'Default|DefOLELCID|DeleteCmdDataSourceType|DeleteCmdDataSource|'
             r'DeleteCmd|DeleteMark|Description|Desktop|'
             r'Details|DisabledBackColor|DisabledForeColor|'
             r'DisabledItemBackColor|DisabledItemForeColor|'
             r'DisabledPicture|DisableEncode|DisplayCount|'
             r'DisplayValue|Dockable|Docked|DockPosition|'
             r'DocumentFile|DownPicture|DragIcon|DragMode|DrawMode|'
             r'DrawStyle|DrawWidth|DynamicAlignment|DynamicBackColor|'
             r'DynamicForeColor|DynamicCurrentControl|DynamicFontBold|'
             r'DynamicFontItalic|DynamicFontStrikethru|'
             r'DynamicFontUnderline|DynamicFontName|DynamicFontOutline|'
             r'DynamicFontShadow|DynamicFontSize|DynamicInputMask|'
             r'DynamicLineHeight|EditorOptions|Enabled|'
             r'EnableHyperlinks|Encrypted|ErrorNo|Exclude|Exclusive|'
             r'FetchAsNeeded|FetchMemoCmdList|FetchMemoDataSourceType|'
             r'FetchMemoDataSource|FetchMemo|FetchSize|'
             r'FileClassLibrary|FileClass|FillColor|FillStyle|Filter|'
             r'FirstElement|FirstNestedTable|Flags|FontBold|FontItalic|'
             r'FontStrikethru|FontUnderline|FontCharSet|FontCondense|'
             r'FontExtend|FontName|FontOutline|FontShadow|FontSize|'
             r'ForceCloseTag|Format|FormCount|FormattedOutput|Forms|'
             r'FractionDigits|FRXDataSession|FullName|GDIPlusGraphics|'
             r'GridLineColor|GridLines|GridLineWidth|HalfHeightCaption|'
             r'HeaderClassLibrary|HeaderClass|HeaderHeight|Height|'
             r'HelpContextID|HideSelection|HighlightBackColor|'
             r'HighlightForeColor|HighlightStyle|HighlightRowLineWidth|'
             r'HighlightRow|Highlight|HomeDir|Hours|HostName|'
             r'HScrollSmallChange|hWnd|Icon|IncrementalSearch|Increment|'
             r'InitialSelectedAlias|InputMask|InsertCmdDataSourceType|'
             r'InsertCmdDataSource|InsertCmdRefreshCmd|'
             r'InsertCmdRefreshFieldList|InsertCmdRefreshKeyFieldList|'
             r'InsertCmd|Instancing|IntegralHeight|'
             r'Interval|IMEMode|IsAttribute|IsBase64|IsBinary|IsNull|'
             r'IsDiffGram|IsLoaded|ItemBackColor,|ItemData|ItemIDData|'
             r'ItemTips|IXMLDOMElement|KeyboardHighValue|KeyboardLowValue|'
             r'Keyfield|KeyFieldList|KeyPreview|KeySort|LanguageOptions|'
             r'LeftColumn|Left|LineContents|LineNo|LineSlant|LinkMaster|'
             r'ListCount|ListenerType|ListIndex|ListItemID|ListItem|'
             r'List|LockColumnsLeft|LockColumns|LockScreen|MacDesktop|'
             r'MainFile|MapN19_4ToCurrency|MapBinary|MapVarchar|Margin|'
             r'MaxButton|MaxHeight|MaxLeft|MaxLength|MaxRecords|MaxTop|'
             r'MaxWidth|MDIForm|MemberClassLibrary|MemberClass|'
             r'MemoWindow|Message|MinButton|MinHeight|MinWidth|'
             r'MouseIcon|MousePointer|Movable|MoverBars|MultiSelect|'
             r'Name|NestedInto|NewIndex|NewItemID|NextSiblingTable|'
             r'NoCpTrans|NoDataOnLoad|NoData|NullDisplay|'
             r'NumberOfElements|Object|OLEClass|OLEDragMode|'
             r'OLEDragPicture|OLEDropEffects|OLEDropHasData|'
             r'OLEDropMode|OLEDropTextInsertion|OLELCID|'
             r'OLERequestPendingTimeout|OLEServerBusyRaiseError|'
             r'OLEServerBusyTimeout|OLETypeAllowed|OneToMany|'
             r'OpenViews|OpenWindow|Optimize|OrderDirection|Order|'
             r'OutputPageCount|OutputType|PageCount|PageHeight|'
             r'PageNo|PageOrder|Pages|PageTotal|PageWidth|'
             r'PanelLink|Panel|ParentAlias|ParentClass|ParentTable|'
             r'Parent|Partition|PasswordChar|PictureMargin|'
             r'PicturePosition|PictureSpacing|PictureSelectionDisplay|'
             r'PictureVal|Picture|Prepared|'
             r'PolyPoints|PreserveWhiteSpace|PreviewContainer|'
             r'PrintJobName|Procedure|PROCESSID|ProgID|ProjectHookClass|'
             r'ProjectHookLibrary|ProjectHook|QuietMode|'
             r'ReadCycle|ReadLock|ReadMouse|ReadObject|ReadOnly|'
             r'ReadSave|ReadTimeout|RecordMark|RecordSourceType|'
             r'RecordSource|RefreshAlias|'
             r'RefreshCmdDataSourceType|RefreshCmdDataSource|RefreshCmd|'
             r'RefreshIgnoreFieldList|RefreshTimeStamp|RelationalExpr|'
             r'RelativeColumn|RelativeRow|ReleaseType|Resizable|'
             r'RespectCursorCP|RespectNesting|RightToLeft|RotateFlip|'
             r'Rotation|RowColChange|RowHeight|RowSourceType|'
             r'RowSource|ScaleMode|SCCProvider|SCCStatus|ScrollBars|'
             r'Seconds|SelectCmd|SelectedID|'
             r'SelectedItemBackColor|SelectedItemForeColor|Selected|'
             r'SelectionNamespaces|SelectOnEntry|SelLength|SelStart|'
             r'SelText|SendGDIPlusImage|SendUpdates|ServerClassLibrary|'
             r'ServerClass|ServerHelpFile|ServerName|'
             r'ServerProject|ShowTips|ShowInTaskbar|ShowWindow|'
             r'Sizable|SizeBox|SOM|Sorted|Sparse|SpecialEffect|'
             r'SpinnerHighValue|SpinnerLowValue|SplitBar|StackLevel|'
             r'StartMode|StatusBarText|StatusBar|Stretch|StrictDateEntry|'
             r'Style|TabIndex|Tables|TabOrientation|Tabs|TabStop|'
             r'TabStretch|TabStyle|Tag|TerminateRead|Text|Themes|'
             r'ThreadID|TimestampFieldList|TitleBar|ToolTipText|'
             r'TopIndex|TopItemID|Top|TwoPassProcess|TypeLibCLSID|'
             r'TypeLibDesc|TypeLibName|Type|Unicode|UpdatableFieldList|'
             r'UpdateCmdDataSourceType|UpdateCmdDataSource|'
             r'UpdateCmdRefreshCmd|UpdateCmdRefreshFieldList|'
             r'UpdateCmdRefreshKeyFieldList|UpdateCmd|'
             r'UpdateGramSchemaLocation|UpdateGram|UpdateNameList|UpdateType|'
             r'UseCodePage|UseCursorSchema|UseDeDataSource|UseMemoSize|'
             r'UserValue|UseTransactions|UTF8Encoded|Value|VersionComments|'
             r'VersionCompany|VersionCopyright|VersionDescription|'
             r'VersionNumber|VersionProduct|VersionTrademarks|Version|'
             r'VFPXMLProgID|ViewPortHeight|ViewPortLeft|'
             r'ViewPortTop|ViewPortWidth|VScrollSmallChange|View|Visible|'
             r'VisualEffect|WhatsThisButton|WhatsThisHelpID|WhatsThisHelp|'
             r'WhereType|Width|WindowList|WindowState|WindowType|WordWrap|'
             r'WrapCharInCDATA|WrapInCDATA|WrapMemoInCDATA|XMLAdapter|'
             r'XMLConstraints|XMLNameIsXPath|XMLNamespace|XMLName|'
             r'XMLPrefix|XMLSchemaLocation|XMLTable|XMLType|'
             r'XSDfractionDigits|XSDmaxLength|XSDtotalDigits|'
             r'XSDtype|ZoomBox)', Name.Attribute),

            (r'\.(ActivateCell|AddColumn|AddItem|AddListItem|AddObject|'
             r'AddProperty|AddTableSchema|AddToSCC|Add|'
             r'ApplyDiffgram|Attach|AutoFit|AutoOpen|Box|Build|'
             r'CancelReport|ChangesToCursor|CheckIn|CheckOut|Circle|'
             r'CleanUp|ClearData|ClearStatus|Clear|CloneObject|CloseTables|'
             r'Close|Cls|CursorAttach|CursorDetach|CursorFill|'
             r'CursorRefresh|DataToClip|DelayedMemoFetch|DeleteColumn|'
             r'Dock|DoMessage|DoScroll|DoStatus|DoVerb|Drag|Draw|Eval|'
             r'GetData|GetDockState|GetFormat|GetKey|GetLatestVersion|'
             r'GetPageHeight|GetPageWidth|Help|Hide|IncludePageInOutput|'
             r'IndexToItemID|ItemIDToIndex|Item|LoadXML|Line|Modify|'
             r'MoveItem|Move|Nest|OLEDrag|OnPreviewClose|OutputPage|'
             r'Point|Print|PSet|Quit|ReadExpression|ReadMethod|'
             r'RecordRefresh|Refresh|ReleaseXML|Release|RemoveFromSCC|'
             r'RemoveItem|RemoveListItem|RemoveObject|Remove|'
             r'Render|Requery|RequestData|ResetToDefault|Reset|Run|'
             r'SaveAsClass|SaveAs|SetAll|SetData|SetFocus|SetFormat|'
             r'SetMain|SetVar|SetViewPort|ShowWhatsThis|Show|'
             r'SupportsListenerType|TextHeight|TextWidth|ToCursor|'
             r'ToXML|UndoCheckOut|Unnest|UpdateStatus|WhatsThisMode|'
             r'WriteExpression|WriteMethod|ZOrder)', Name.Function),

            (r'\.(Activate|AdjustObjectSize|AfterBand|AfterBuild|'
             r'AfterCloseTables|AfterCursorAttach|AfterCursorClose|'
             r'AfterCursorDetach|AfterCursorFill|AfterCursorRefresh|'
             r'AfterCursorUpdate|AfterDelete|AfterInsert|'
             r'AfterRecordRefresh|AfterUpdate|AfterDock|AfterReport|'
             r'AfterRowColChange|BeforeBand|BeforeCursorAttach|'
             r'BeforeCursorClose|BeforeCursorDetach|BeforeCursorFill|'
             r'BeforeCursorRefresh|BeforeCursorUpdate|BeforeDelete|'
             r'BeforeInsert|BeforeDock|BeforeOpenTables|'
             r'BeforeRecordRefresh|BeforeReport|BeforeRowColChange|'
             r'BeforeUpdate|Click|dbc_Activate|dbc_AfterAddTable|'
             r'dbc_AfterAppendProc|dbc_AfterCloseTable|dbc_AfterCopyProc|'
             r'dbc_AfterCreateConnection|dbc_AfterCreateOffline|'
             r'dbc_AfterCreateTable|dbc_AfterCreateView|dbc_AfterDBGetProp|'
             r'dbc_AfterDBSetProp|dbc_AfterDeleteConnection|'
             r'dbc_AfterDropOffline|dbc_AfterDropTable|'
             r'dbc_AfterModifyConnection|dbc_AfterModifyProc|'
             r'dbc_AfterModifyTable|dbc_AfterModifyView|dbc_AfterOpenTable|'
             r'dbc_AfterRemoveTable|dbc_AfterRenameConnection|'
             r'dbc_AfterRenameTable|dbc_AfterRenameView|'
             r'dbc_AfterValidateData|dbc_BeforeAddTable|'
             r'dbc_BeforeAppendProc|dbc_BeforeCloseTable|'
             r'dbc_BeforeCopyProc|dbc_BeforeCreateConnection|'
             r'dbc_BeforeCreateOffline|dbc_BeforeCreateTable|'
             r'dbc_BeforeCreateView|dbc_BeforeDBGetProp|'
             r'dbc_BeforeDBSetProp|dbc_BeforeDeleteConnection|'
             r'dbc_BeforeDropOffline|dbc_BeforeDropTable|'
             r'dbc_BeforeModifyConnection|dbc_BeforeModifyProc|'
             r'dbc_BeforeModifyTable|dbc_BeforeModifyView|'
             r'dbc_BeforeOpenTable|dbc_BeforeRemoveTable|'
             r'dbc_BeforeRenameConnection|dbc_BeforeRenameTable|'
             r'dbc_BeforeRenameView|dbc_BeforeValidateData|'
             r'dbc_CloseData|dbc_Deactivate|dbc_ModifyData|dbc_OpenData|'
             r'dbc_PackData|DblClick|Deactivate|Deleted|Destroy|DoCmd|'
             r'DownClick|DragDrop|DragOver|DropDown|ErrorMessage|Error|'
             r'EvaluateContents|GotFocus|Init|InteractiveChange|KeyPress|'
             r'LoadReport|Load|LostFocus|Message|MiddleClick|MouseDown|'
             r'MouseEnter|MouseLeave|MouseMove|MouseUp|MouseWheel|Moved|'
             r'OLECompleteDrag|OLEDragOver|OLEGiveFeedback|OLESetData|'
             r'OLEStartDrag|OnMoveItem|Paint|ProgrammaticChange|'
             r'QueryAddFile|QueryModifyFile|QueryNewFile|QueryRemoveFile|'
             r'QueryRunFile|QueryUnload|RangeHigh|RangeLow|ReadActivate|'
             r'ReadDeactivate|ReadShow|ReadValid|ReadWhen|Resize|'
             r'RightClick|SCCInit|SCCDestroy|Scrolled|Timer|UIEnable|'
             r'UnDock|UnloadReport|Unload|UpClick|Valid|When)', Name.Function),

            (r'\s+', Text),
            # everything else is not colored
            (r'.', Text),
        ],
        'newline': [
            (r'\*.*?$', Comment.Single, '#pop'),
            (r'(ACCEPT|ACTIVATE\s*MENU|ACTIVATE\s*POPUP|ACTIVATE\s*SCREEN|'
             r'ACTIVATE\s*WINDOW|APPEND|APPEND\s*FROM|APPEND\s*FROM\s*ARRAY|'
             r'APPEND\s*GENERAL|APPEND\s*MEMO|ASSIST|AVERAGE|BLANK|BROWSE|'
             r'BUILD\s*APP|BUILD\s*EXE|BUILD\s*PROJECT|CALCULATE|CALL|'
             r'CANCEL|CHANGE|CLEAR|CLOSE|CLOSE\s*MEMO|COMPILE|CONTINUE|'
             r'COPY\s*FILE|COPY\s*INDEXES|COPY\s*MEMO|COPY\s*STRUCTURE|'
             r'COPY\s*STRUCTURE\s*EXTENDED|COPY\s*TAG|COPY\s*TO|'
             r'COPY\s*TO\s*ARRAY|COUNT|CREATE|CREATE\s*COLOR\s*SET|'
             r'CREATE\s*CURSOR|CREATE\s*FROM|CREATE\s*LABEL|CREATE\s*MENU|'
             r'CREATE\s*PROJECT|CREATE\s*QUERY|CREATE\s*REPORT|'
             r'CREATE\s*SCREEN|CREATE\s*TABLE|CREATE\s*VIEW|DDE|'
             r'DEACTIVATE\s*MENU|DEACTIVATE\s*POPUP|DEACTIVATE\s*WINDOW|'
             r'DECLARE|DEFINE\s*BAR|DEFINE\s*BOX|DEFINE\s*MENU|'
             r'DEFINE\s*PAD|DEFINE\s*POPUP|DEFINE\s*WINDOW|DELETE|'
             r'DELETE\s*FILE|DELETE\s*TAG|DIMENSION|DIRECTORY|DISPLAY|'
             r'DISPLAY\s*FILES|DISPLAY\s*MEMORY|DISPLAY\s*STATUS|'
             r'DISPLAY\s*STRUCTURE|DO|EDIT|EJECT|EJECT\s*PAGE|ERASE|'
             r'EXIT|EXPORT|EXTERNAL|FILER|FIND|FLUSH|FUNCTION|GATHER|'
             r'GETEXPR|GO|GOTO|HELP|HIDE\s*MENU|HIDE\s*POPUP|'
             r'HIDE\s*WINDOW|IMPORT|INDEX|INPUT|INSERT|JOIN|KEYBOARD|'
             r'LABEL|LIST|LOAD|LOCATE|LOOP|MENU|MENU\s*TO|MODIFY\s*COMMAND|'
             r'MODIFY\s*FILE|MODIFY\s*GENERAL|MODIFY\s*LABEL|MODIFY\s*MEMO|'
             r'MODIFY\s*MENU|MODIFY\s*PROJECT|MODIFY\s*QUERY|'
             r'MODIFY\s*REPORT|MODIFY\s*SCREEN|MODIFY\s*STRUCTURE|'
             r'MODIFY\s*WINDOW|MOVE\s*POPUP|MOVE\s*WINDOW|NOTE|'
             r'ON\s*APLABOUT|ON\s*BAR|ON\s*ERROR|ON\s*ESCAPE|'
             r'ON\s*EXIT\s*BAR|ON\s*EXIT\s*MENU|ON\s*EXIT\s*PAD|'
             r'ON\s*EXIT\s*POPUP|ON\s*KEY|ON\s*KEY\s*=|ON\s*KEY\s*LABEL|'
             r'ON\s*MACHELP|ON\s*PAD|ON\s*PAGE|ON\s*READERROR|'
             r'ON\s*SELECTION\s*BAR|ON\s*SELECTION\s*MENU|'
             r'ON\s*SELECTION\s*PAD|ON\s*SELECTION\s*POPUP|ON\s*SHUTDOWN|'
             r'PACK|PARAMETERS|PLAY\s*MACRO|POP\s*KEY|POP\s*MENU|'
             r'POP\s*POPUP|PRIVATE|PROCEDURE|PUBLIC|PUSH\s*KEY|'
             r'PUSH\s*MENU|PUSH\s*POPUP|QUIT|READ|READ\s*MENU|RECALL|'
             r'REINDEX|RELEASE|RELEASE\s*MODULE|RENAME|REPLACE|'
             r'REPLACE\s*FROM\s*ARRAY|REPORT|RESTORE\s*FROM|'
             r'RESTORE\s*MACROS|RESTORE\s*SCREEN|RESTORE\s*WINDOW|'
             r'RESUME|RETRY|RETURN|RUN|RUN\s*\/N"|RUNSCRIPT|'
             r'SAVE\s*MACROS|SAVE\s*SCREEN|SAVE\s*TO|SAVE\s*WINDOWS|'
             r'SCATTER|SCROLL|SEEK|SELECT|SET|SET\s*ALTERNATE|'
             r'SET\s*ANSI|SET\s*APLABOUT|SET\s*AUTOSAVE|SET\s*BELL|'
             r'SET\s*BLINK|SET\s*BLOCKSIZE|SET\s*BORDER|SET\s*BRSTATUS|'
             r'SET\s*CARRY|SET\s*CENTURY|SET\s*CLEAR|SET\s*CLOCK|'
             r'SET\s*COLLATE|SET\s*COLOR\s*OF|SET\s*COLOR\s*OF\s*SCHEME|'
             r'SET\s*COLOR\s*SET|SET\s*COLOR\s*TO|SET\s*COMPATIBLE|'
             r'SET\s*CONFIRM|SET\s*CONSOLE|SET\s*CURRENCY|SET\s*CURSOR|'
             r'SET\s*DATE|SET\s*DEBUG|SET\s*DECIMALS|SET\s*DEFAULT|'
             r'SET\s*DELETED|SET\s*DELIMITERS|SET\s*DEVELOPMENT|'
             r'SET\s*DEVICE|SET\s*DISPLAY|SET\s*DOHISTORY|SET\s*ECHO|'
             r'SET\s*ESCAPE|SET\s*EXACT|SET\s*EXCLUSIVE|SET\s*FIELDS|'
             r'SET\s*FILTER|SET\s*FIXED|SET\s*FORMAT|SET\s*FULLPATH|'
             r'SET\s*FUNCTION|SET\s*HEADINGS|SET\s*HELP|SET\s*HELPFILTER|'
             r'SET\s*HOURS|SET\s*INDEX|SET\s*INTENSITY|SET\s*KEY|'
             r'SET\s*KEYCOMP|SET\s*LIBRARY|SET\s*LOCK|SET\s*LOGERRORS|'
             r'SET\s*MACDESKTOP|SET\s*MACHELP|SET\s*MACKEY|SET\s*MARGIN|'
             r'SET\s*MARK\s*OF|SET\s*MARK\s*TO|SET\s*MEMOWIDTH|'
             r'SET\s*MESSAGE|SET\s*MOUSE|SET\s*MULTILOCKS|SET\s*NEAR|'
             r'SET\s*NOCPTRANS|SET\s*NOTIFY|SET\s*ODOMETER|SET\s*OPTIMIZE|'
             r'SET\s*ORDER|SET\s*PALETTE|SET\s*PATH|SET\s*PDSETUP|'
             r'SET\s*POINT|SET\s*PRINTER|SET\s*PROCEDURE|SET\s*READBORDER|'
             r'SET\s*REFRESH|SET\s*RELATION|SET\s*RELATION\s*OFF|'
             r'SET\s*REPROCESS|SET\s*RESOURCE|SET\s*SAFETY|SET\s*SCOREBOARD|'
             r'SET\s*SEPARATOR|SET\s*SHADOWS|SET\s*SKIP|SET\s*SKIP\s*OF|'
             r'SET\s*SPACE|SET\s*STATUS|SET\s*STATUS\s*BAR|SET\s*STEP|'
             r'SET\s*STICKY|SET\s*SYSMENU|SET\s*TALK|SET\s*TEXTMERGE|'
             r'SET\s*TEXTMERGE\s*DELIMITERS|SET\s*TOPIC|SET\s*TRBETWEEN|'
             r'SET\s*TYPEAHEAD|SET\s*UDFPARMS|SET\s*UNIQUE|SET\s*VIEW|'
             r'SET\s*VOLUME|SET\s*WINDOW\s*OF\s*MEMO|SET\s*XCMDFILE|'
             r'SHOW\s*GET|SHOW\s*GETS|SHOW\s*MENU|SHOW\s*OBJECT|'
             r'SHOW\s*POPUP|SHOW\s*WINDOW|SIZE\s*POPUP|SKIP|SORT|'
             r'STORE|SUM|SUSPEND|TOTAL|TYPE|UNLOCK|UPDATE|USE|WAIT|'
             r'ZAP|ZOOM\s*WINDOW|DO\s*CASE|CASE|OTHERWISE|ENDCASE|'
             r'DO\s*WHILE|ENDDO|FOR|ENDFOR|NEXT|IF|ELSE|ENDIF|PRINTJOB|'
             r'ENDPRINTJOB|SCAN|ENDSCAN|TEXT|ENDTEXT|=)',
                Keyword.Reserved, '#pop'),
            (r'#\s*(IF|ELIF|ELSE|ENDIF|DEFINE|IFDEF|IFNDEF|INCLUDE)',
                Comment.Preproc, '#pop'),
            (r'(m\.)?[a-z_]\w*', Name.Variable, '#pop'),
            (r'.', Text, '#pop'),
        ],
    }