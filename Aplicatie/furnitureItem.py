
from PyQt5.QtWidgets import QGraphicsPixmapItem, QMenu, QGraphicsRectItem
from PyQt5.QtCore import QPointF,Qt
from PyQt5.QtGui import QTransform, QPen

class FurnitureItem(QGraphicsPixmapItem):
    def __init__(self, pixmap,item_type):
        super().__init__(pixmap)
        self.setFlag(QGraphicsPixmapItem.ItemIsMovable)
        self.original_pixmap = pixmap
        self.rotation_angle = 0
        self.item_type = item_type

        self.temp_border = QGraphicsRectItem(self.boundingRect(), self)
        self.temp_border.setPen(QPen(Qt.transparent))
        self.setPos(100, 100)
        self.initial_pos = self.pos()

    def mouseMoveEvent(self, event):
        self.old_pos = self.pos()
        super().mouseMoveEvent(event)

        self.checkBorderWithItems()
        diff_pos = self.pos() - self.old_pos

        self.temp_border.setRect(self.boundingRect())
        self.temp_border.setPos(diff_pos)

        self.setZValue(1)
        self.bringToFront()
        self.mousePressEvent(event)

    def checkCollisions(self):
        other_Items = self.scene().items()


        for item in other_Items:

            if isinstance(item,QGraphicsRectItem) and item != self and item.zValue() == 0.1 and self.collidesWithItem(item):
                print(item.pos())
                self.setPos(self.initial_pos)
            if isinstance(item, FurnitureItem) and item != self and self.item_type != "Plant":
                if item.item_type == "Carpet":
                    pass
                elif self.collidesWithItem(item):
                    self.setPos(self.initial_pos)
            if isinstance(item,FurnitureItem) and item.item_type == "Plant" and self.item_type == "Plant" and item !=self and self.collidesWithItem(item):
                self.setPos(self.initial_pos)




    def checkBorderWithItems(self):
        other_Items = self.scene().items()

        collision_detected = False

        for item in other_Items:
            if isinstance(item, QGraphicsRectItem) and item != self and item.zValue() == 0.1 and self.collidesWithItem(item):
                collision_detected = True
                break

            if isinstance(item, FurnitureItem) and item != self and self.item_type != "Plant":
                if item.item_type == "Carpet":
                    continue

                if self.collidesWithItem(item):
                    collision_detected = True
                    break


            if isinstance(item,FurnitureItem) and item.item_type == "Plant" and self.item_type == "Plant" and item != self:
                if self.collidesWithItem(item):
                    collision_detected = True
                    break
        if not (0 <= self.x() <= self.scene().width() - self.boundingRect().width() and
                0 <= self.y() <= self.scene().height() - self.boundingRect().height()):
            collision_detected = True


        if collision_detected:
            self.temp_border.setPen(QPen(Qt.red))
        else:
            self.temp_border.setPen(QPen(Qt.green))


    def mouseReleaseEvent(self, event):
        new_pos = self.pos()
        if (0 <= new_pos.x() <= self.scene().width() - self.boundingRect().width() and
                0 <= new_pos.y() <= self.scene().height() - self.boundingRect().height()):

            self.checkCollisions()

            super().mouseReleaseEvent(event)

        else:
            x = min(max(new_pos.x(), 0), self.scene().width() - self.boundingRect().width())
            y = min(max(new_pos.y(), 0), self.scene().height() - self.boundingRect().height())
            self.setPos(QPointF(x, y))
            self.checkCollisions()

        self.temp_border.setPen(QPen(Qt.transparent))
        self.initial_pos = self.pos()

    def bringToFront(self):
        scene = self.scene()

        if scene is not None:
            items = scene.items()
            max_z = max(item.zValue() for item in items)
            self.setZValue(max_z + 1)

    def itemChange(self, change, value):
        if change == QGraphicsPixmapItem.ItemPositionChange:
            new_rect = self.mapToScene(value).boundingRect()
            scene_rect = self.scene().sceneRect()

            if not scene_rect.contains(new_rect):
                new_value = QPointF(
                    min(max(new_rect.left(), scene_rect.left()), scene_rect.right() - new_rect.width()),
                    min(max(new_rect.top(), scene_rect.top()), scene_rect.bottom() - new_rect.height())
                )
                return new_value

        return super().itemChange(change, value)

    def contextMenuEvent(self, event):
        context_menu = QMenu(self.scene().views()[0])

        rotate_action = context_menu.addAction("Rotate")
        delete_action = context_menu.addAction("Delete")

        action = context_menu.exec_(event.screenPos())

        if action == rotate_action:
            self.rotation_angle += 90
            rotated_pixmap = self.original_pixmap.transformed(QTransform().rotate(self.rotation_angle))
            self.setPixmap(rotated_pixmap)
        elif action == delete_action:
            self.scene().removeItem(self)