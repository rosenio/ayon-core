from qtpy.QtCore import QSettings

class UiSettingsMixin:
    def setup_settings(self, settings_group: str, default_size=(800, 600)):
        self.settings = QSettings("Ayon", "Ayon_Settings")
        self.settings_group = settings_group
        self.default_size = default_size
        self.restore_window_settings()

    def restore_window_settings(self):
        self.settings.beginGroup(self.settings_group)
        geometry = self.settings.value("geometry")
        if geometry:
            self.restoreGeometry(geometry)
        else:
            self.resize(*self.default_size)
        self.settings.endGroup()

    def save_window_settings(self):
        self.settings.beginGroup(self.settings_group)
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.endGroup()

    def closeEvent(self, event):
        self.save_window_settings()
        super().closeEvent(event)

    def quitEvent(self, event):
        self.save_window_settings()
        super().closeEvent(event)