import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HostPlotComponent } from './host-plot.component';

describe('HostPlotComponent', () => {
  let component: HostPlotComponent;
  let fixture: ComponentFixture<HostPlotComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HostPlotComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HostPlotComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
