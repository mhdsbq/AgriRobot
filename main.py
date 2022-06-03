import imp
from go_distance_forward import go_distance_forward
from get_disease_report import get_disease_report
from sync_report_with_backend import sync_report_with_backend

go_distance_forward(10)
disease_report = get_disease_report()
response = sync_report_with_backend(disease_report)

print("done")