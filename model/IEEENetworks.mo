within ;
package IEEENetworks "Different networks from IEEE"
  model IEEE_9Bus
    PowerSystems.Electrical.Branches.PwLine line(
      G=0,
      R=0.0119,
      X=0.1008,
      B=0.1045) annotation (Placement(transformation(
          extent={{-10,-10},{10,10}},
          rotation=180,
          origin={22,50})));
    PowerSystems.Electrical.Branches.PwLine line1(
      G=0,
      R=0.0085,
      X=0.072,
      B=0.0745) annotation (Placement(transformation(
          extent={{-10,-10},{10,10}},
          rotation=0,
          origin={-29,50})));
    PowerSystems.Electrical.Buses.Bus B2
      annotation (Placement(transformation(extent={{-108,37},{-82,63}})));
    PowerSystems.Electrical.Buses.Bus B7
      annotation (Placement(transformation(extent={{-68,38},{-42,64}})));
    PowerSystems.Electrical.Buses.Bus B9
      annotation (Placement(transformation(extent={{31,37},{58,64}})));
    PowerSystems.Electrical.Buses.Bus B3
      annotation (Placement(transformation(extent={{69,37},{95,63}})));
    PowerSystems.Electrical.Branches.PwLine line2(
      G=0,
      R=0.039,
      X=0.170,
      B=0.179) annotation (Placement(visible=true, transformation(
          origin={40,20},
          extent={{-10,-10},{10,10}},
          rotation=90)));
    PowerSystems.Electrical.Branches.PwLine line3(
      G=0,
      R=0.032,
      X=0.161,
      B=0.153) annotation (Placement(visible=true, transformation(
          origin={-60,20},
          extent={{-10,-10},{10,10}},
          rotation=90)));
    PowerSystems.Electrical.Buses.Bus B8 annotation (Placement(visible=true,
          transformation(
          origin={-1,51},
          extent={{-13,-13},{13,13}},
          rotation=180)));
    PowerSystems.Electrical.Buses.Bus B6 annotation (Placement(visible=true,
          transformation(
          origin={41,-12},
          extent={{-14,-14},{14,14}},
          rotation=-90)));
    PowerSystems.Electrical.Buses.Bus B5 annotation (Placement(visible=true,
          transformation(
          origin={-48,-13},
          extent={{-14,-14},{14,14}},
          rotation=-90)));
    PowerSystems.Electrical.Branches.PwLine line5(
      R=0.017,
      X=0.092,
      G=0,
      B=0.079) annotation (Placement(visible=true, transformation(
          origin={40,-31},
          extent={{-10,-10},{10,10}},
          rotation=90)));
    PowerSystems.Electrical.Branches.PwLine line4(
      G=0,
      R=0.01,
      X=0.085,
      B=0.088) annotation (Placement(visible=true, transformation(
          origin={-48,-32},
          extent={{-10,-10},{10,10}},
          rotation=90)));
    PowerSystems.Electrical.Buses.Bus B4 annotation (Placement(visible=true,
          transformation(
          origin={-1,-48},
          extent={{-13,-13},{13,13}},
          rotation=-90)));
    PowerSystems.Electrical.Buses.Bus B1 annotation (Placement(visible=true,
          transformation(
          origin={0,-86},
          extent={{-13,-13},{13,13}},
          rotation=-90)));
    UserDefined.ieee9bus_configBus2 ieee9bus_configbus21 annotation(Placement(visible = true, transformation(origin = {-120, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
    UserDefined.ieee9bus_configBus3 ieee9bus_configbus31 annotation(Placement(visible = true, transformation(origin = {110, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
    PowerSystems.Electrical.Loads.PSSE.ConstantLoad constantLoad(
      a(re=1, im=0),
      b(re=0, im=1),
      PQBRAK=0.7,
      S_i(re=0, im=0),
      S_y(re=0, im=0),
      S_p(re=1.25, im=0.50),
      v0=0.9975267,
      anglev0=-3.984869) annotation (Placement(transformation(
          extent={{-10,-10},{10,10}},
          rotation=-90,
          origin={-72,-21})));
    PowerSystems.Electrical.Loads.PSSE.ConstantLoad constantLoad1(
      a(re=1, im=0),
      b(re=0, im=1),
      S_i(re=0, im=0),
      S_y(re=0, im=0),
      v0=1.013555,
      anglev0=-3.685885,
      S_p(re=0.90, im=0.3),
      PQBRAK=0.7) annotation (Placement(transformation(
          extent={{-10,-10},{10,10}},
          rotation=-90,
          origin={73,-17})));
    PowerSystems.Electrical.Loads.PSSE.ConstantLoad constantLoad2(
      a(re=1, im=0),
      b(re=0, im=1),
      PQBRAK=0.7,
      S_i(re=0, im=0),
      S_y(re=0, im=0),
      v0=1.018439,
      anglev0=0.7034081,
      S_p(re=1, im=0.35)) annotation (Placement(transformation(
          extent={{-10,-10},{10,10}},
          rotation=-90,
          origin={15,65})));
    PowerSystems.Electrical.Events.PwFault pwFault(
      t1=0.1,
      t2=0.2,
      R=0,
      X=0,
      ground=0)
              annotation (Placement(transformation(extent={{5,1},{25,21}})));
    PowerSystems.Electrical.Branches.PSSE.TwoWindingTransformer
      twoWindingTransformer3(
      R=0,
      G=0,
      B=0,
      X=0.0625,
      t1=1,
      t2=1,
      PrimaryOnFromSide=true)
      annotation (Placement(transformation(extent={{-87,40},{-67,60}})));
    PowerSystems.Electrical.Branches.PSSE.TwoWindingTransformer
      twoWindingTransformer2(
      R=0,
      X=0.0576,
      G=0,
      B=0,
      t1=1,
      t2=1,
      PrimaryOnFromSide=true) annotation (Placement(transformation(
          extent={{-10,-10},{10,10}},
          rotation=90,
          origin={1,-67})));
    PowerSystems.Electrical.Branches.PSSE.TwoWindingTransformer
      twoWindingTransformer1(
      R=0,
      G=0,
      B=0,
      X=0.0586,
      t1=1,
      t2=1,
      PrimaryOnFromSide=true) annotation (Placement(transformation(
          extent={{-10,-10},{10,10}},
          rotation=180,
          origin={63,51})));
    UserDefined.ieee9bus_configBus1_2 ieee9bus_configBus1_2_1
      annotation (Placement(transformation(extent={{-57,-113},{-17,-91}})));
  equation
    connect(ieee9bus_configbus21.pwpin1, B2.p)
      annotation (Line(points={{-110,50},{-95,50}}, color={0,0,255}));
    connect(B4.p, line5.p) annotation (Line(points={{-1,-48},{-1,-48},{-1,-40},
            {-1,-38},{40,-38}},color={0,0,255}));
    connect(B4.p, line4.p)
      annotation (Line(points={{-1,-48},{-1,-39},{-48,-39}},
                                                           color={0,0,255}));
    connect(line5.n, B6.p)
      annotation (Line(points={{40,-24},{40,-12},{41,-12}}, color={0,0,255}));
    connect(line4.n, B5.p) annotation (Line(points={{-48,-25},{-47,-25},{-47,
            -13},{-48,-13}}, color={0,0,255}));
    connect(constantLoad.p, B5.p) annotation (Line(points={{-71,-14},{-71,-14},
            {-71,-7},{-49,-7},{-49,-13},{-48,-13}}, color={0,0,255}));
    connect(B6.p, constantLoad1.p) annotation (Line(points={{41,-12},{42,-12},{
            42,-7},{74,-7},{74,-10}}, color={0,0,255}));
    connect(B6.p, line2.p) annotation (Line(points={{41,-12},{41,-12},{41,13},{
            40,13}}, color={0,0,255}));
    connect(B5.p, line3.p) annotation (Line(points={{-48,-13},{-47,-13},{-47,3},
            {-57,3},{-57,13},{-60,13}}, color={0,0,255}));
    connect(B7.p, line3.n) annotation (Line(points={{-55,51},{-53,51},{-53,50},
            {-49,50},{-49,27},{-60,27}}, color={0,0,255}));
    connect(line2.n, B9.p) annotation (Line(points={{40,27},{37,27},{37,50.5},{
            44.5,50.5}}, color={0,0,255}));
    connect(B8.p, line.n) annotation (Line(points={{-1,51},{7,51},{7,50},{15,50}},
          color={0,0,255}));
    connect(line.p, B9.p) annotation (Line(points={{29,50},{37,50},{37,50.5},{
            44.5,50.5}}, color={0,0,255}));
    connect(B7.p, line1.p) annotation (Line(points={{-55,51},{-42,51},{-42,50},
            {-36,50}}, color={0,0,255}));
    connect(line1.n, B8.p) annotation (Line(points={{-22,50},{-12,50},{-12,51},
            {-1,51}}, color={0,0,255}));
    connect(B8.p, constantLoad2.p) annotation (Line(points={{-1,51},{-5,51},{-5,
            57},{-9,57},{-9,79},{16,79},{16,72}}, color={0,0,255}));
    connect(B3.p, ieee9bus_configbus31.pwpin1)
      annotation (Line(points={{82,50},{105.714,50},{105.714,50}},
                                                           color={0,0,255}));
    connect(B8.p, pwFault.p) annotation (Line(points={{-1,51},{-1,32},{8,32},{8,
            12}}, color={0,0,255}));
    connect(B7.p, twoWindingTransformer3.n) annotation (Line(points={{-55,51},{
            -63,51},{-63,50.2},{-70,50.2}}, color={0,0,255}));
    connect(B2.p, twoWindingTransformer3.p) annotation (Line(points={{-95,50},{
            -89.5,50},{-89.5,50.2},{-84,50.2}}, color={0,0,255}));
    connect(twoWindingTransformer2.n, B4.p) annotation (Line(points={{0.8,-60},
            {-1,-60},{-1,-48}},         color={0,0,255}));
    connect(twoWindingTransformer1.p, B3.p) annotation (Line(points={{70,50.8},
            {76,50.8},{76,50},{82,50}}, color={0,0,255}));
    connect(twoWindingTransformer1.n, B9.p) annotation (Line(points={{56,50.8},
            {51.5,50.8},{51.5,50.5},{44.5,50.5}}, color={0,0,255}));
    connect(B1.p, twoWindingTransformer2.p)
      annotation (Line(points={{0,-86},{0,-74},{0.8,-74}}, color={0,0,255}));
    connect(ieee9bus_configBus1_2_1.pwpin1, B1.p)
      annotation (Line(points={{-20,-103},{0,-103},{0,-86}}, color={0,0,255}));
    annotation(Diagram(coordinateSystem(extent={{-160,-120},{150,100}},      preserveAspectRatio=false,   initialScale = 0.1, grid = {1, 1})), Icon(coordinateSystem(extent={{-160,
              -120},{150,100}},                                                                                                    preserveAspectRatio = false, initialScale = 0.1, grid = {1, 1})));
  end IEEE_9Bus;

  package UserDefined "Component models with different configuration each"
    model ieee9bus_configBus1

      PowerSystems.Connectors.PwPin pwpin1 annotation (Placement(
          visible=true,
          transformation(
            origin={100,0},
            extent={{-5,-5},{5,5}},
            rotation=0),
          iconTransformation(
            origin={100,0},
            extent={{-10,-10},{10,10}},
            rotation=0)));
      PowerSystems.Electrical.Machines.PSSE.GENSAL.GENSAL gensal1(
        Mbase=275,
        Tpd0=8.96,
        Tppd0=0.05,
        Tppq0=0.05,
        H=9.55,
        D=1.6,
        Xd=0.3615,
        Xq=0.24,
        Xpd=0.1508,
        Xppd=0.1,
        Xppq=0.1,
        Xl=0.06,
        s10=1.01,
        s12=1.02,
        Sbase=100,
        eterm=1.04,
        anglev0=0,
        pelec=71.61309,
        qelec=25.59159) annotation (Placement(visible=true, transformation(
            origin={14,-0.5},
            extent={{-53,-44.5},{53,44.5}},
            rotation=0)));
      PowerSystems.Electrical.Controls.PSSE.ES.IEEET1.IEEET1 ieeet11(
        TR=0.0,
        KA=20.0,
        TA=0.2,
        VRMAX=3.0,
        VRMIN=-3.0,
        KE=1.0,
        TE=0.314,
        KF=0.063,
        TF=0.35,
        E1=2.8,
        SE1=0.3034,
        E2=3.73,
        SE2=1.2884,
        Ec0=1.04) annotation (Placement(visible=true, transformation(
            origin={-83.0746,15.5},
            extent={{-54.9254,-54.5},{47.0746,54.5}},
            rotation=0)));
      PowerSystems.Electrical.Controls.PSSE.TG.IEESGO ieesgo1(
        T1=25,
        T2=0.0,
        T3=1.0,
        T4=1.0,
        T5=12.5,
        T6=0.0,
        K1=5.0,
        K2=3.0,
        K3=0.5,
        PMAX=1.0,
        PMIN=0.0) annotation (Placement(visible=true, transformation(
            origin={-115.5,87.5},
            extent={{-68.5,-35.5},{68.5,35.5}},
            rotation=0)));
      PowerSystems.Electrical.Controls.PSSE.PSS.PSS2A.PSS2A pss2a1(
        T_w1=2,
        T_w2=2,
        T_6=0,
        T_w3=2,
        T_w4=4,
        T_7=2,
        K_S2=0.250,
        K_S3=1,
        T_8=0.5,
        T_9=0.1,
        K_S1=30,
        T_1=0.150,
        T_2=0.03,
        T_3=0.15,
        T_4=0.03,
        M=0,
        N=0) annotation (Placement(visible=true, transformation(
            origin={-219.998,23.7145},
            extent={{-31.0017,-11.7145},{61.9962,29.2857}},
            rotation=0)));
      Modelica.Blocks.Sources.Constant const(k=0)
                                             annotation(Placement(visible = true, transformation(origin={-217,-8},    extent={{-10,-10},
                {10,10}},                                                                                                    rotation = 0)));
    equation
      connect(gensal1.p, pwpin1) annotation(Line(points={{51.1,0.39},{80.0753,
              0.39},{80.0753,0},{100,0}},                                                                                          color = {0, 0, 255}));
      connect(gensal1.EFD0, ieeet11.EFD0) annotation (Line(points={{48.98,
              -28.98},{56,-28.98},{56,-60},{-159,-60},{-159,-14.475},{-125.054,
              -14.475}}, color={0,0,127}));
      connect(gensal1.ETERM, ieeet11.EC) annotation (Line(points={{48.98,19.08},
              {87,19.08},{87,-71},{-175,-71},{-175,-4.665},{-125.054,-4.665}},
            color={0,0,127}));
      connect(ieesgo1.PMECH, gensal1.PMECH) annotation (Line(points={{-68.92,
              87.5},{-49,87.5},{-49,25.31},{-23.1,25.31}}, color={0,0,127}));
      connect(gensal1.PMECH0, ieesgo1.PMECH0) annotation (Line(points={{48.98,
              -11.18},{87,-11.18},{87,59},{-170,59},{-170,77.205},{-162.08,
              77.205}}, color={0,0,127}));
      connect(gensal1.SPEED, ieesgo1.SPEED) annotation (Line(points={{48.98,
              37.77},{83,37.77},{83,108},{-175,108},{-175,94.245},{-162.08,
              94.245}}, color={0,0,127}));
      connect(ieeet11.EFD, gensal1.EFD) annotation (Line(points={{-41.8846,
              -0.85},{-35.3396,-0.85},{-35.3396,-1.39},{-22.04,-1.39}}, color={
              0,0,127}));
      connect(pss2a1.VOTHSG, ieeet11.VOTHSG) annotation (Line(points={{-156.142,
              32.5001},{-133,32.5001},{-133,17.135},{-125.054,17.135}}, color={
              0,0,127}));
      connect(gensal1.PELEC, pss2a1.V_S2) annotation (Line(points={{48.98,
              -20.08},{71,-20.08},{71,-82},{-262,-82},{-262,22.2501},{-250.38,
              22.2501}}, color={0,0,127}));
      connect(gensal1.SPEED, pss2a1.V_S1) annotation (Line(points={{48.98,37.77},
              {55,37.77},{55,112},{-267,112},{-267,42.7502},{-250.38,42.7502}},
            color={0,0,127}));
      connect(const.y, ieeet11.VOEL) annotation (Line(points={{-206,-8},{-198,
              -8},{-185,-8},{-185,10},{-125.054,10},{-125.054,10.595}}, color={
              0,0,127}));
      connect(const.y, ieeet11.VUEL) annotation (Line(points={{-206,-8},{-172,
              -8},{-172,2.965},{-125.054,2.965}}, color={0,0,127}));
      annotation(Diagram(coordinateSystem(extent={{-270,-100},{130,120}},      preserveAspectRatio=false,  initialScale = 0.1, grid = {1, 1})), Icon(coordinateSystem(extent={{-270,
                -100},{130,120}},                                                                                                    preserveAspectRatio = true, initialScale = 0.1, grid = {1, 1}), graphics={  Ellipse(origin=  {0, 49.3056}, extent=  {{-99.2063, -148.512}, {99.2063, 49.9008}}, endAngle=  360), Ellipse(origin=  {14.9802, -0.198413}, extent=  {{-34.4246, -39.2857}, {64.3849, 39.6825}}, endAngle=  360), Line(origin=  {30.1605, 0.00179934}, points=  {{-29.9621, -20.0415}, {-10.3193, 20.0379}, {9.91884, -20.0415}, {29.9585, 20.0379}, {29.9585, 20.0379}}), Text(origin=  {-61.71, 12.1}, extent=  {{-17.66, 27.38}, {31.15, -51.59}}, textString=  "GENSAL &\n IEEET1 &\n IEESGO &\n PSS2A", fontName=  "Andalus", textStyle=  {TextStyle.Italic})}));
    end ieee9bus_configBus1;

    model ieee9bus_configBus2

      PowerSystems.Connectors.PwPin pwpin1 annotation (Placement(
          visible=true,
          transformation(
            origin={100,0},
            extent={{-5,-5},{5,5}},
            rotation=0),
          iconTransformation(
            origin={100,0},
            extent={{-10,-10},{10,10}},
            rotation=0)));
      PowerSystems.Electrical.Machines.PSSE.GENROU.GENROU genrou1(
        Tppd0=0.05,
        s10=1.01,
        s12=1.02,
        eterm=1.03,
        Sbase=100,
        Tpd0=6,
        Tpq0=0.5350,
        Tppq0=0.05,
        D=0.67,
        Xd=1.72,
        Xq=1.66,
        Xpd=0.2300,
        Xpq=0.3700,
        Xppd=0.2100,
        Xppq=0.2100,
        Xl=0.1,
        anglev0=9.182196,
        pelec=163,
        qelec=8.925101,
        H=3.330,
        Mbase=320) annotation (Placement(visible=true, transformation(
            origin={31,9.5},
            extent={{-49,-45.5},{49,45.5}},
            rotation=0)));
    equation
      connect(genrou1.p, pwpin1) annotation (Line(points={{65.3,9.5},{77.175,
              9.5},{77.175,0},{100,0}}, color={0,0,255}));
      connect(genrou1.PMECH0, genrou1.PMECH) annotation (Line(points={{64.32,
              -11.43},{88,-11.43},{88,61},{-20,61},{-20,36},{-3.3,36},{-3.3,
              36.8}}, color={0,0,127}));
      connect(genrou1.EFD0, genrou1.EFD) annotation (Line(points={{64.32,-20.53},
              {75,-20.53},{75,-50},{-35,-50},{-35,18.6},{-3.3,18.6}}, color={0,
              0,127}));
      annotation(Diagram(coordinateSystem(extent={{-180,-100},{100,100}},      preserveAspectRatio=false,  initialScale = 0.1, grid = {1, 1})), Icon(coordinateSystem(extent={{-180,
                -100},{100,100}},                                                                                                    preserveAspectRatio = true, initialScale = 0.1, grid = {1, 1}), graphics={  Ellipse(origin=  {0, 0.0992063}, extent=  {{-99.2063, -99.504}, {99.4048, 99.1071}}, endAngle=  360), Ellipse(origin=  {29.9603, -0.0992063}, extent=  {{-49.2063, -39.3849}, {49.2063, 39.3849}}, endAngle=  360), Line(origin=  {30.0604, 0.100096}, points=  {{-29.862, -19.9414}, {-10.0207, 19.9396}, {9.82054, -19.9414}, {29.8602, 19.9396}, {29.8602, 19.9396}}), Text(origin=  {-54.86, -0.2}, extent=  {{-24.3, 39.48}, {24.11, -39.09}}, textString=  "GENROU &\n IEEET1 &\n IEESGO &\n PSS2A", fontName=  "Andalus", textStyle=  {TextStyle.Italic})}));
    end ieee9bus_configBus2;

    model ieee9bus_configBus3

      PowerSystems.Electrical.Machines.PSSE.GENROU.GENROU genrou1(
        Tpd0=5.89,
        Tppd0=0.05,
        Tpq0=0.6,
        Tppq0=0.05,
        H=2.35,
        D=0.47,
        Xd=1.68,
        Xq=1.61,
        Xpd=0.2321,
        Xpq=0.32,
        Xppd=0.21,
        Xl=0.1536,
        s10=1.01,
        s12=1.02,
        eterm=1.025,
        Sbase=100,
        anglev0=4.647661,
        pelec=85,
        qelec=-12.50314,
        Mbase=300) annotation (Placement(visible=true, transformation(
            origin={-2.5,14.5},
            extent={{-62.5,-44.5},{62.5,44.5}},
            rotation=0)));
      PowerSystems.Connectors.PwPin pwpin1 annotation (Placement(
          visible=true,
          transformation(
            origin={100,0},
            extent={{-5,-5},{5,5}},
            rotation=0),
          iconTransformation(
            origin={100,0},
            extent={{-10,-10},{10,10}},
            rotation=0)));
    equation
      connect(genrou1.p, pwpin1) annotation(Line(points={{41.25,14.5},{79.7928,
              14.5},{79.7928,0.141226},{100,0.141226},{100,0}},                                                                                     color = {0, 0, 255}));
      connect(genrou1.PMECH0, genrou1.PMECH) annotation (Line(points={{40,-5.97},
              {68,-5.97},{68,72},{-60,72},{-60,41.2},{-46.25,41.2}}, color={0,0,
              127}));
      connect(genrou1.EFD0, genrou1.EFD) annotation (Line(points={{40,-14.87},{
              61,-14.87},{61,-45},{-82,-45},{-82,23.4},{-46.25,23.4}}, color={0,
              0,127}));
      annotation(Diagram(coordinateSystem(extent={{-180,-100},{100,100}},      preserveAspectRatio=false,  initialScale = 0.1, grid = {1, 1})), Icon(coordinateSystem(extent={{-180,
                -100},{100,100}},                                                                                                    preserveAspectRatio = true, initialScale = 0.1, grid = {1, 1}), graphics={  Ellipse(origin=  {0, 0.0992063}, extent=  {{-99.2063, -99.504}, {99.2063, 99.3056}}, endAngle=  360), Ellipse(origin=  {30.0595, -0.0992063}, extent=  {{-49.504, -39.1865}, {49.3056, 39.5833}}, endAngle=  360), Line(origin=  {29.9884, -0.170374}, points=  {{-29.7899, -19.8693}, {-9.94867, 20.0116}, {9.8926, -19.8693}, {29.9323, 20.2101}, {30.1307, 20.2101}}), Text(origin=  {-60.02, 0.2}, extent=  {{-19.94, 39.88}, {29.4638, -39.4832}}, textString=  "GENROU &\n IEEET1 &\n IEESGO &\n PSS2A", fontName=  "Andalus", textStyle=  {TextStyle.Italic})}));
    end ieee9bus_configBus3;

    model ieee9bus_configBus1_2

      PowerSystems.Connectors.PwPin pwpin1 annotation (Placement(
          visible=true,
          transformation(
            origin={100,0},
            extent={{-5,-5},{5,5}},
            rotation=0),
          iconTransformation(
            origin={100,0},
            extent={{-10,-10},{10,10}},
            rotation=0)));
      PowerSystems.Electrical.Machines.PSSE.GENSAL.GENSAL gensal1(
        Tpd0=8.96,
        Tppd0=0.05,
        Tppq0=0.05,
        H=9.55,
        D=1.6,
        Xd=0.3615,
        Xq=0.24,
        Xpd=0.1508,
        Xppd=0.1,
        Xppq=0.1,
        Xl=0.06,
        s10=1.01,
        s12=1.02,
        Sbase=100,
        eterm=1.04,
        anglev0=0,
        pelec=71.61309,
        qelec=25.59159,
        Mbase=275) annotation (Placement(visible=true, transformation(
            origin={14,-0.5},
            extent={{-53,-44.5},{53,44.5}},
            rotation=0)));
    equation
      connect(gensal1.p, pwpin1) annotation(Line(points={{51.1,0.39},{80.0753,
              0.39},{80.0753,0},{100,0}},                                                                                          color = {0, 0, 255}));
      connect(gensal1.PMECH0, gensal1.PMECH) annotation (Line(points={{48.98,
              -11.18},{81,-11.18},{81,75},{-66,75},{-66,25.31},{-23.1,25.31}},
            color={0,0,127}));
      connect(gensal1.EFD0, gensal1.EFD) annotation (Line(points={{48.98,-28.98},
              {60,-28.98},{60,-62},{-57,-62},{-57,-1.39},{-22.04,-1.39}}, color=
             {0,0,127}));
      annotation(Diagram(coordinateSystem(extent={{-270,-100},{130,120}},      preserveAspectRatio=false,  initialScale = 0.1, grid = {1, 1})), Icon(coordinateSystem(extent={{-270,
                -100},{130,120}},                                                                                                    preserveAspectRatio = true, initialScale = 0.1, grid = {1, 1}), graphics={  Ellipse(origin=  {0, 49.3056}, extent=  {{-99.2063, -148.512}, {99.2063, 49.9008}}, endAngle=  360), Ellipse(origin=  {14.9802, -0.198413}, extent=  {{-34.4246, -39.2857}, {64.3849, 39.6825}}, endAngle=  360), Line(origin=  {30.1605, 0.00179934}, points=  {{-29.9621, -20.0415}, {-10.3193, 20.0379}, {9.91884, -20.0415}, {29.9585, 20.0379}, {29.9585, 20.0379}}), Text(origin=  {-61.71, 12.1}, extent=  {{-17.66, 27.38}, {31.15, -51.59}}, textString=  "GENSAL &\n IEEET1 &\n IEESGO &\n PSS2A", fontName=  "Andalus", textStyle=  {TextStyle.Italic})}));
    end ieee9bus_configBus1_2;
  end UserDefined;
  annotation(uses(                             Modelica(version="3.2.1"),
        PowerSystems(version="0.5")));
end IEEENetworks;
