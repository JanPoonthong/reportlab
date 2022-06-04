# Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.samples.excelcolors import *
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, String
from reportlab.graphics.charts.textlabels import Label


class ClusteredBar(_DrawingEditorMixin, Drawing):
    def __init__(self, width=200, height=150, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        self._add(
            self,
            HorizontalBarChart(),
            name="chart",
            validate=None,
            desc="The main chart",
        )
        self.chart.width = 115
        self.chart.height = 80
        self.chart.x = 30
        self.chart.y = 40
        self.chart.bars[0].fillColor = color01
        self.chart.bars[1].fillColor = color02
        self.chart.bars[2].fillColor = color03
        self.chart.bars[3].fillColor = color04
        self.chart.bars[4].fillColor = color05
        self.chart.bars[5].fillColor = color06
        self.chart.bars[6].fillColor = color07
        self.chart.bars[7].fillColor = color08
        self.chart.bars[8].fillColor = color09
        self.chart.bars[9].fillColor = color10
        self.chart.fillColor = backgroundGrey
        self.chart.barLabels.fontName = "Helvetica"
        self.chart.valueAxis.labels.fontName = "Helvetica"
        self.chart.valueAxis.labels.fontSize = 6
        self.chart.valueAxis.forceZero = 1
        self.chart.data = [(100, 150, 180), (125, 180, 200)]
        self.chart.groupSpacing = 15
        self.chart.valueAxis.avoidBoundFrac = 1
        self.chart.valueAxis.gridEnd = 80
        self.chart.valueAxis.tickDown = 3
        self.chart.valueAxis.visibleGrid = 1
        self.chart.categoryAxis.categoryNames = ["North", "South", "Central"]
        self.chart.categoryAxis.tickLeft = 3
        self.chart.categoryAxis.labels.fontName = "Helvetica"
        self.chart.categoryAxis.labels.fontSize = 6
        self.chart.categoryAxis.labels.dx = -3
        self._add(
            self,
            Label(),
            name="Title",
            validate=None,
            desc="The title at the top of the chart",
        )
        self.Title.fontName = "Helvetica-Bold"
        self.Title.fontSize = 7
        self.Title.x = 100
        self.Title.y = 135
        self.Title._text = "Chart Title"
        self.Title.maxWidth = 180
        self.Title.height = 20
        self.Title.textAnchor = "middle"
        self._add(
            self,
            Legend(),
            name="Legend",
            validate=None,
            desc="The legend or key for the chart",
        )
        self.Legend.colorNamePairs = [
            (color01, "Widgets"),
            (color02, "Sprockets"),
        ]
        self.Legend.fontName = "Helvetica"
        self.Legend.fontSize = 7
        self.Legend.x = 153
        self.Legend.y = 85
        self.Legend.dxTextSpace = 5
        self.Legend.dy = 5
        self.Legend.dx = 5
        self.Legend.deltay = 5
        self.Legend.alignment = "right"
        self._add(
            self,
            Label(),
            name="XLabel",
            validate=None,
            desc="The label on the horizontal axis",
        )
        self.XLabel.fontName = "Helvetica"
        self.XLabel.fontSize = 7
        self.XLabel.x = 85
        self.XLabel.y = 10
        self.XLabel.textAnchor = "middle"
        self.XLabel.maxWidth = 100
        self.XLabel.height = 20
        self.XLabel._text = "X Axis"
        self._add(
            self,
            Label(),
            name="YLabel",
            validate=None,
            desc="The label on the vertical axis",
        )
        self.YLabel.fontName = "Helvetica"
        self.YLabel.fontSize = 7
        self.YLabel.x = 12
        self.YLabel.y = 80
        self.YLabel.angle = 90
        self.YLabel.textAnchor = "middle"
        self.YLabel.maxWidth = 100
        self.YLabel.height = 20
        self.YLabel._text = "Y Axis"
        self._add(self, 0, name="preview", validate=None, desc=None)


if __name__ == "__main__":  # NORUNTESTS
    ClusteredBar().save(formats=["pdf"], outDir=None, fnRoot="clustered_bar")
