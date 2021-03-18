import { TestBed } from '@angular/core/testing';

import { HostDetailToPlotService } from './host-detail-to-plot.service';

describe('HostDetailToPlotService', () => {
  let service: HostDetailToPlotService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HostDetailToPlotService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
